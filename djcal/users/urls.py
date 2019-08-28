# users/urls.py
from django.urls import path
from django.conf.urls import url

from .views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]
