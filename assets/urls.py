from django.urls import path
from . import views

app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
]