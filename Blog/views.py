from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Blog.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    return render(request,'Blog/index.html')