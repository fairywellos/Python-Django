from django.urls import path

from qlabs import views


urlpatterns = [
    path('', views.LogList.as_view()),
    path('add', views.index),
    path('chart', views.ChartView.as_view(), name='Chart'),
    path('chart_data', views.ChartData.as_view()),
]