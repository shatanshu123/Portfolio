from django.shortcuts import render,get_object_or_404
from .models import Job
def Shatanshu(request):
    job=Job.objects
    return render(request,'jobs/home.html', {'jobs':job})

def details(request,job_id):
    job_details=get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/details.html',{'job':job_details})