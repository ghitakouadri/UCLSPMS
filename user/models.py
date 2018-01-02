from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User
from project.models import Project,Keyword
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.core.mail import send_mail

class InterestQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=True)

    def inactive(self):
        return self.filter(status=False)


class InterestManager(models.Manager):
    def get_queryset(self):
        return InterestQuerySet(self.model,using=self._db)

    def active(self):
        return self.get_queryset().active()

    def inactive(self):
        return self.get_queryset().inactive()

class ProfileManager(models.Manager):
    pass

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    status = models.BooleanField(default=False)
    objects = InterestManager()


class Invitation(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
        (3, 'Done'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    objects = InterestManager()


    def __str__(self):
            return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(default=1)
    birth_date = models.DateField(null=True, blank=True)
    preferences = models.ManyToManyField(Keyword)
    avatar = models.FileField(default="https://www.w3schools.com/w3css/img_fjords.jpg")
    linkedin = models.URLField(blank=True)
    objects = models.Manager()



@receiver(post_save,sender=Invitation)
def create_invitation(sender,instance,created,**kwargs):
  if created:
    subject = "You have received a notificaion from {}.".format("Notice Project")
    message = "Dear Sir/Madam\n This is the link to create a staff account\n\n Link: localhost:8000/user/invitation/{}\n".format(instance.id)
    from_email = 'contact.dataspartan@gmail.com'
    to_email = [instance.email]
    send_mail(subject,message,from_email,to_email,fail_silently=False)



@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:

        try:
         if instance.type == 2:
                profile  = Profile.objects.create(user=instance,type=2)
                print("profile")
                print(profile.profile)
         elif instance.type == 3:
                profile  = Profile.objects.create(user=instance,type=3)
         else:
              print("type == 1")
              Profile.objects.create(user=instance,type=1)
        except:
              Profile.objects.create(user=instance,type=1)



@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
