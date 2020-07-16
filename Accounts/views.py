from django.shortcuts import redirect, render, get_object_or_404, reverse
from .forms import *
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method=='POST':
        form=signupform(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pas = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=pas)
            login(request, user)
            return redirect('/')
    else:
        form=signupform()
    context={
        'form':form,
    }
    return render(request,'signup.html',context)


@login_required(login_url="/accounts/login/")
def profile(request):
    p = get_object_or_404(Profile,user=request.user)
    context={
        'p':p,
    }

    return render(request,'profile.html',context)

@login_required
def edite_profile(request):
    p = get_object_or_404(Profile, user=request.user)
    if request.method=='POST':
        u_form = signupform(request.POST, request.FILES, instance=request.user)
        p_form=profileform(request.POST,request.FILES,instance=p)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('Accounts:profile')
    else:
        u_form = signupform(instance=request.user)
        p_form = profileform(instance=p)
    context={
        'u_form': u_form,
        'p_form':p_form,
    }
    return render(request, 'edite_profile.html', context)






















