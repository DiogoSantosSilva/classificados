from django.shortcuts import render
from django.http import HttpResponse
from .models import Job

def test(request):
     template_name = 'index.html'

     jobs = Job.objects.all()

     context = {"title": "Classificados", "jobs": jobs}
     return render(request, template_name, context)