from django.shortcuts import render , redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from app1.models import Post
from .forms import userRegisterForm,Updateuesrform,Update_Profile

def register(request):
    if request.method== 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'account has been created to {username}')
            form.save()
            return redirect('login')

    else:
        form =userRegisterForm()
    return render(request,'userapp/register.html',{'form':form})



@login_required()
def profile(request):


    return render(request , 'userapp/proflie.html')








@login_required()
def UpdateProfile(request):
    if request.method == 'POST':
        form_user=Updateuesrform( request.POST ,instance=request.user)
        form_profile=Update_Profile(request.POST,request.FILES,instance=request.user.profile)
        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()
            return redirect('profile')

    else:
        form_user = Updateuesrform(instance=request.user)
        form_profile = Update_Profile(instance=request.user.profile)


    context={'FU':form_user,'FP':form_profile}

    return render(request , 'userapp/UpdateProfile.html',context)