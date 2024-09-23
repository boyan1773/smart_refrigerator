from django.shortcuts import render
from .predict import ai
# Create your views here.
def home (request):
    ai()
    return render(request,'home.html')
