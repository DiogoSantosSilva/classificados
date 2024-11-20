from .models import Job
from django.forms import ModelForm

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ["title", "description"]