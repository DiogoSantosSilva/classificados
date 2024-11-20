
from django.contrib import admin
from django.urls import path
from job.views import home, create_edit_job

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/job', create_edit_job)
]
