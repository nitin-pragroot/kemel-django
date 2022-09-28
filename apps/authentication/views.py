

# Create your views here.
from django.contrib.auth.forms import SetPasswordForm
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from .forms import LoginForm, SignUpForm
from apps.helpers import *
from apps import COMMON, helpers
from core.settings import GITHUB_AUTH
from django.contrib.auth import get_user_model
User = get_user_model()


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            # Credentials ok
            if user:
                login(request, user)
                return redirect("/")
            
            # Check user is registered
            user = username_exists(username)
            if user:
                user = email_exists(username)
                msg = "Incorrect Username / Password please try again."
        else:
            msg = 'Error validating the form'
    else:
        msg = request.GET.get('message', None)

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):

    msg     = None
    success = False

    # new Registration
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
        
            form.save()
        
            username     = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            
            user         = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            #return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def change_password(request, **kwargs):

    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        message = 'Password successfully changed.'
        status = 200
    else:
        message = form.errors
        status = 400
    return JsonResponse({
        'message': message
    }, status=status)


def delete_account(request, **kwargs):
    result, message = helpers.delete_user(request.user.username)
    if not result:
        return JsonResponse({
            'errors': message
        }, status=400)
    logout(request)
    return HttpResponseRedirect('/login/')
