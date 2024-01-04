from django.shortcuts import render
from django.http import HttpResponse
from .models import T


def home(request):
    t = T.objects.all()
    return render(request,'home.html', {'t':t})
