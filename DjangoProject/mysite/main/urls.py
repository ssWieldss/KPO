from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('register', views.register, name='register'),
  path('authorization', views.authorization, name='authorization'),
  path('creation', views.creation, name='creation'),
]
