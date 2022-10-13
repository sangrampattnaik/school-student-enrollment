from django.urls import path

from . import views

urlpatterns = [
    path("school/", views.SchoolCreateAPIView.as_view()),
    path("student/", views.StudentCreateAPIView.as_view()),
    path("login/", views.LoginAPIView.as_view()),
]
