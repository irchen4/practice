from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admins', views.adminis),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logoutUser)
]