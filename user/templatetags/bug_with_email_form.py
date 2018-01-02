from django import template
from ..forms import  BugWithEmailForm
register = template.Library()

@register.simple_tag
def bug_with_email_form():
    return BugWithEmailForm()
