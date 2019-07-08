from django.urls import path

from qlabs import views

urlpatterns = [
    path('', views.LogList.as_view()),
]