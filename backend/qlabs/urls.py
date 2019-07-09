from django.urls import path

from qlabs import views


urlpatterns = [
    path('', views.LiveTableView.as_view()),
    path('live', views.LiveTableView.as_view()),
    path('test', views.TestTableView.as_view()),
    path('monthly', views.MonthlyTableView.as_view()),
    path('add', views.index),
    path('chart', views.ChartView.as_view(), name='Chart'),
    path('chart_data', views.ChartData.as_view()),
]