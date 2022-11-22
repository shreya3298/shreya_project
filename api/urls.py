from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('get/',views.UserList.as_view(),name="get"),
    path('post/',views.UserCreate.as_view(),name ='post'),
     path('put/<int:pk>', views.UserPut.as_view(), name='put'),
    path('delete/<int:pk>', views.UserDelete.as_view(), name='delete'),

]



