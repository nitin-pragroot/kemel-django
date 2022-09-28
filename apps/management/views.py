from django import template
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from apps import COMMON
from apps.authentication.models import CustomUser


@login_required(login_url="/login/")
def index(request):
    if CustomUser.objects.get(username=request.user.username).status == COMMON.USER_SUSPENDED:
        logout(request)
        return redirect(reverse(f'login') + f'?message=Suspended account. Please contact support.', )
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

