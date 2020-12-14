from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage.as_view()),
    path('about/', views.about.as_view()),
    path('contacts/', views.contacts.as_view())
]