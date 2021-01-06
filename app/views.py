from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginuser,logout 
from .models import TRACKER
from .forms import TRACKERForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        form = TRACKERForm
        user=request.user
        trackers = TRACKER.objects.filter(user=user)
        context = {
            'form':form,
            'trackers':trackers
        }
        return render(request,'index.html',context)

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {
            'form':form
        }
        return render(request,'signup.html',context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect("login")
        else:
            return render(request,'signup.html',context)

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request,'login.html',context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                loginuser(request,user)
                return redirect('home') 
        else:
            context = {
                'form':form
            }
            return render(request,'login.html',context)

@login_required(login_url='login')
def add_tracker(request):
    print(request.user)
    print("hello")
    if request.user.is_authenticated:
        form = TRACKERForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.user = request.user
            tracker.save()
            print(request.user)
            return redirect('home')
        else:
            return render(request,'index.html',context={'form':form})

def delete_tracker(request,id):
    TRACKER.objects.get(pk=id).delete()
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')
    

            

