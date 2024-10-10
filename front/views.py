from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from .frms import AddForm
from django.contrib import messages
from .forms import *
from .models import *
import pandas as pd
import openpyxl

# Create your views here.
def index(request):
    
    return render(request, 'index.html', )

def Home(request):
     
    form = AddForm()

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = AddForm()


    return render(request, 'home.html', context)


def Sign(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        psw1 = request.POST.get('password1')
        psw2 = request.POST.get('password2')

        if psw1 != psw2:
            return HttpResponse('Your passwords do not Match !!!')
        else:
            user_details = Users(uname=uname, email=email, psw1=psw1)
            user_details.save()

        return HttpResponseRedirect('login')

    return render(request, 'signup.html')


def Login(request):

    return render(request, 'login.html')



