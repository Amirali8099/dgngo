from django.shortcuts import render
from django.shortcuts import render


def about_us(request):
    return render(request, 'about_us/about_us.html')


# Create your views here.
