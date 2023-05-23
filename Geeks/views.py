from django.shortcuts import render
from Geeks.forms import GeeksForms
from .models import GeeksModels

from django.forms import modelformset_factory
# Create your views here.

def formset_view(request):
    context = {}

    # creating form set 
    GeeksFormSet = modelformset_factory(GeeksModels, fields =['title', 'description'], extra = 3)
    formset = GeeksFormSet()
    # adding form set to context
    context['formset']= formset
    return render(request,'home.html',context)