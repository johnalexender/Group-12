from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('funding', views.funding, name='funding'),
    path('investment_history/<str:member_name>/',views.member_info, name='member_info'),
    
]
