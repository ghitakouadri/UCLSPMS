from django.test import TestCase, RequestFactory
import json
# Create your tests here.
from ..views import ProjectUpdateView,ProjectCreateView
import datetime
from ..models import Keyword,Project,Organization
from user.models import Interest
from cuser.models import CUser as User



class ProjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(email="siewml9512223@gmail.")
        number_of_projects = 13
        cls.organization = Organization.objects.create(title="UCL",status=True)
        cls.organization.save()

        for project_num in range(number_of_projects):
            Project.objects.create(title="Test Project {}".format(project_num),summary="testing project",slug="test-project-{}".format(project_num),organization=cls.organization,created_by=user,status=2,deadline=(datetime.date.today() + datetime.timedelta(days=1)))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/project/')
        self.assertEqual(resp.status_code,200)

    def test_view_url_uses_correct_template(self):
        resp = self.client.get('/project/')
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"project/index.html")

    def test_pagination_is_ten(self):
        resp = self.client.get('/project/')
        self.assertEqual(resp.status_code,200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        print(resp.context['object_list'])
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_list_all_projects(self):
        resp = self.client.get('/project/?page=2',{})
        print(resp)
        self.assertEqual(resp.status_code,200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 3)


class ProjectCreateViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(email='testuser1',password='12345')
        test_user2 = User.objects.create_user(email='testuser2',password='12345')
        test_user1.save()
        test_user2.save()
        test_user1.profile.type = 1
        test_user1.profile.is_verified = True
        test_user1.profile.save()
        test_user2.profile.type = 3
        test_user2.profile.is_verified = True
        test_user2.profile.save()
        self.organization = Organization.objects.create(title="UCL",status=True)
        self.organization.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get('/project/create/')
        self.assertRedirects(resp,'/user/login/?next=/project/create/')

    def test_redirect_if_is_student(self):
        login = self.client.login(email='testuser1', password='12345')
        print("login")
        resp = self.client.get('/project/create/')
        self.assertRedirects(resp,'/user/profile/')

    '''def test_logged_in_uses_correct_template(self):
        login = self.client.login(email='testuser2', password='12345')
        user = User.objects.get(id=2)
        resp = self.client.get('/project/create/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(str(resp.context['user']), 'testuser2')
        self.assertTemplateUsed(resp, 'project/create.html')'''

    def test_post(self):
        login = self.client.login(email='testuser2', password='12345')
        user = User.objects.get(id=1)

        data = {
           'title' : 'Project',
           "summary":"testing project",
           "slug":"test-project",
           "organization":self.organization.id,
           "deadline":datetime.date(year=2100, month=1,day=1),
           "status" : 2
        }
        response = self.client.post("/project/create/", data)
        self.assertEqual(response.status_code, 302)
        project = Project.objects.get(id=1)
        self.assertEqual(project.id,1)


class ProjectDetailViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(email='testuser1')
        user.save()
        self.organization = Organization.objects.create(title="UCL",status=True)
        self.organization.save()
        project = Project.objects.create(title="Test Project",status=2,summary="testing project",slug="test-project",organization=self.organization,created_by=user,deadline=datetime.datetime.now())
        project.save()
    def test_get(self):
        resp = self.client.get('/project/single/test-project/')
        created_project = Project.objects.get(id=1)
        print(resp.context['object'])
        project = resp.context['object']
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'project/detail.html')
        self.assertEqual(project,project)

class ProjectUpdateViewTest(TestCase):
    def setUp(self):
            self.factory = RequestFactory()
            Keyword.objects.create(title="keyword",type=1)
            test_user1 = User.objects.create_user(email='testuser1',password='12345')
            test_user2 = User.objects.create_user(email='testuser2',password='12345')

            test_user1.save()
            test_user2.save()
            test_user1.profile.type = 3
            test_user1.profile.is_verified = True
            test_user1.profile.save()
            test_user2.profile.type = 3
            test_user2.profile.is_verified = True
            test_user2.profile.save()
            self.organization = Organization.objects.create(title="UCL",status=True)
            self.organization.save()
            Project.objects.create(title="Test Project",summary="testing project",slug="test-project",organization=self.organization,created_by=test_user2,status=2,deadline=datetime.datetime.now() )

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get('/project/1/update/')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp,'/user/login/?next=/project/1/update/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(email='testuser2', password='12345')
        user = User.objects.get(id=2)
        resp = self.client.get('/project/1/update/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'project/create.html')

    def test_redirect_if_not_creator(self):
        login = self.client.login(email='testuser1', password='12345')
        print("resp")
        try:
          resp = self.client.get('/project/1/update/')
          self.assertFalse(1,1)
        except TypeError:
          self.assertTrue(1,1)

    def test_post(self):
        login = self.client.login(email='testuser2', password='12345')
        user = User.objects.get(id=2)
        print(user.profile.__dict__)
        current_project = Project.objects.get(id=1)
        data = {
                   'title' : 'Project',
                   "summary":"testing project",
                   "company":"UCL",
                   "deadline":datetime.date(year=2100, month=1,day=1),
                   "status" : 2,
                   "keywords" : [1]
                }
        response = self.client.post("/project/1/update/", data)

        print(response)
        self.assertEqual(response.status_code, 302)
        project = Project.objects.get(id=1)
        print(project.title)
        self.assertFalse(project.title == current_project.title)

class ProjectDetailAjaxRecommendation(TestCase):
    def setUp(self):
        user = User.objects.create_user(email="username1")
        Keyword.objects.create(title="Test Keyword",type=1,status=True)
        Keyword.objects.create(title="Test Keyword 2",type=1,status=True)
        Keyword.objects.create(title="Test Keyword 3",type=1,status=True)
        Keyword.objects.create(title="Test Keyword 4",type=1,status=True)
        Keyword.objects.create(title="Test Keyword 5",type=1,status=True)
        Keyword.objects.create(title="Test Keyword 6",type=1,status=True)
        Keyword.objects.create(title="Test Keyword 7",type=1,status=True)
        self.organization = Organization.objects.create(title="UCL",status=True)
        self.organization.save()
        self.projects = []
        project = Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [1,2]
        project.save()
        self.projects.append(project)
        project = Project.objects.create(status=2,title="Test Project2",summary="testing project",slug="test-project-2",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [1,2,3]

        project.save()
        self.projects.append(project)

        self.project = project
        project = Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project-3",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [3,4]

        project.save()
        self.projects.append(project)

        project =project_interested = Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project-412",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [1,2,3,5]

        project.save()
        self.projects.append(project)

        project =Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project-4",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [1,2,5]
        project.save()
        self.projects.append(project)

        project =Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project-5",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [2,3,5]
        project.save()
        self.projects.append(project)

        project =Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project-6",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [2,3,4]

        project.save()
        self.projects.append(project)

        project = Project.objects.create(status=2,title="Test Project",summary="testing project",slug="test-project-7",organization=self.organization,created_by=user,deadline=(datetime.datetime.now() + datetime.timedelta(days=1)))
        project.keywords = [2,3,5]
        project.save()
        self.projects.append(project)

        Interest.objects.create(user=user,project=project_interested)

    def test_get(self):
        resp = self.client.get('/project/ajax/getDetailRecommendations/?id={}'.format(self.project.id))
        print("   ")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print('test_get ajax ' )
        print()
        obj = json.loads(((resp._container)[0]).decode('utf-8'))
        projects = obj["keywords"]
        print(projects)
        self.assertEqual(projects[0]["pk"],4)
        self.assertEqual(projects[0]["keyword_count"],3)
        self.assertEqual(resp.status_code, 200)
