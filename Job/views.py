from django.shortcuts import render,reverse, get_object_or_404, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def job_list(request):
    jobs=Job.objects.all()
    paginator=Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'jobs': page_obj,
 
    }
    return render(request,'job_list.html',context)

def job(request,slug):
    job=get_object_or_404(Job,slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            return reverse( "'Job:job' job.id")
    else:
        form = ApplyForm()
    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'job_details.html', context)


@login_required
def add_job(request):
    if request.method=='POST':
        
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
           
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect('/')
    else:
        form = JobForm()
        
    context={
        'form':form,
    }
    return render(request,'add_job.html',context)
