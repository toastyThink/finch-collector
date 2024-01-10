#all paths specific to finchcollector 
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),

   path('about/', views.about, name='about'), 

   path('finches/', views.finches_index, name='index'),

   path('finch/<int:finch_id>/', views.finches_detail,name='detail'),
]