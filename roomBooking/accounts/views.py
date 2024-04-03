from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("userManagement")
    template_name = "registration/signup.html"

# def showUsers(request):
#     data = User.objects.all()
#     users = {'users': data}
#     return render(request, "home.html", users)

def userManagementView(request):
    data = User.objects.all()
    context = {'users': data}
    return render(request, "accounts/userManagement.html", context)

def deleteUserView(request,id):
    user = User.objects.get(id=id)
    context = {'deletingUser' : user}
    return render(request, "accounts/deleteUser.html", context)

def deleteUserRecord(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("home")
