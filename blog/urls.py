from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('post_views/', views.post_views, name="post_views"),
    path('profile/', views.profile, name="profile"),
    path('contacts/', views.contacts, name="contacts"),
    path('resume/', views.resume, name="resume"),
    

]