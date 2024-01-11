#all paths specific to finchcollector 
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),

   path('about/', views.about, name='about'), 

   path('finches/', views.finches_index, name='index'),

   path('finches/<int:finch_id>/', views.finches_detail,name='detail'),

   #.as_view() turns the class CatCreate intoa function to satisfy 
   # the path function's need to have a callback function/param
   path('finch/create/', views.FinchCreate.as_view(), name='finches_create'),

   path('finch/<int:pk>/update/', views.FinchUpdate.as_view(), name="finch_update"),
     #pk is the same thing as cat_id -> pk is django convention
     # the int: converts the following value into an integar -> in this case the number 
     #associated with the finch id for the page -> finch 1

   path('finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete')

]