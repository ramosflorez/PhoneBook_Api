from django.urls import re_path
from phonebook import views
from rest_framework import routers



urlpatterns=[
    re_path(r'^contacts$',views.ContactsApi),
    re_path(r'^Types$',views.TypeofContact),
    re_path(r'^person$',views.PersonApi),
    re_path(r'^Organizations$',views.OrganizationApi),

]