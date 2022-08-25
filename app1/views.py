from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import  ListView,DeleteView,CreateView,UpdateView,DeleteView
# Create your views here.

from django.http import HttpResponse

from .models import Post

posts=[
    {'title': 'First post',
     'auther':'mohamed',
     'content': 'the first use from template post ',
     'date':'9 August 2022 '
     }
    ,
{'title': 'second post',
     'auther':'mohamed',
     'content': 'this step to learn django and use it again for another project  ',
     'date':'9 August 2022 '
     }
]
#Post.objects.all()
'''
def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'Home'
    }
    return  render(request,'app/home.html',context)
'''


def about(request):
    return  render(request,'app/about.html',{'title':'About'})





class postListView(ListView):
    model = Post
    template_name = "app/home.html"
    context_object_name = 'posts'
    ordering = ['-date']




class userpostListView(ListView):
    model = Post
    template_name = "app/user_posts.html"
    context_object_name = 'posts'
    ordering = ['-date']


    def get_queryset(self):
        user = get_object_or_404(User ,username=self.kwargs.get('username'))
        return Post.objects.filter(auther=user)


class postDetailtView(DeleteView):
    model = Post
    template_name = "app/post.html"



class postCreatetView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "app/post_create.html"
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.auther=self.request.user

        return super().form_valid(form)

class postUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = "app/post_create.html"
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.auther=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post =self.get_object()
        return self.request.user==post.auther


class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "app/post_delete.html"
    fields = ['title','content']

    success_url='/'


    def test_func(self):
        post =self.get_object()
        return self.request.user==post.auther