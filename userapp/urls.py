from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='user_register')
    #path('login/',views.login,name='login')

]