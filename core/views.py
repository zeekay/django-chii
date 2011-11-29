from django.shortcuts import render
from django.template import TemplateDoesNotExist

def index(request):
    try:
        return render(request, 'custom_index.html')
    except TemplateDoesNotExist:
        return render(request, 'index.html')
