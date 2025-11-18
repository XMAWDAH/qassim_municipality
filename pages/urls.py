from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('contact/', views.contact, name='contact'),
]
