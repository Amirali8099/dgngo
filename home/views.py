from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return render(request, 'index/index.html')


# Create your views here.
