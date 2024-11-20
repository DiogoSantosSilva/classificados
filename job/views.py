from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Job
from .form import JobForm

def home(request):
    template_name = 'index.html'
    jobs = Job.objects.all()
    context = {"title": "Classificados", "jobs": jobs}
    return render(request, template_name, context)


# GET
def job(request, pk):
    template_name = 'job_detail.html'
    job = Job.objects.get(pk=pk)
    context = {"job": job}
    return render(request, template_name, context)

def create_edit_job(request):
    template_name = 'form.html'
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = JobForm()
    return render(request, template_name, {"form": form})