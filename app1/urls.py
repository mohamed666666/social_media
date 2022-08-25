from django.urls import path
from . import views
from .views import postListView,postDetailtView,postCreatetView,postUpdateView,postDeleteView,userpostListView

urlpatterns = [
    path('', postListView.as_view(),name='app_home'),
    path('user/<username>', userpostListView.as_view(),name='user_posts'),
    path('post/<int:pk>/', postDetailtView.as_view(),name='post_detail'),
    path('post/new/', postCreatetView.as_view(),name='post_create'),
    path('post/<int:pk>/update', postUpdateView.as_view(),name='post_update'),
    path('post/<int:pk>/delete', postDeleteView.as_view(),name='post_delete'),
    path('about/',views.about,name='app1_about')
]
