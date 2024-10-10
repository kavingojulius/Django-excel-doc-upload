from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from .frms import AddForm

# Create your views here.

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
        eml = request.POST.get('email')
        psw1 = request.POST.get('password1')
        psw2 = request.POST.get('password2')

        if psw1 != psw2:
            return HttpResponse('Your passwords do not Match !!!')
        else:
            user_details = User.objects.create_user(uname,eml,psw1)
            user_details.save()

        return HttpResponseRedirect('login')

    return render(request, 'signup.html')


def Login(request):

    return render(request, 'login.html')



