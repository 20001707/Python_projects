from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

def agent_only(view_func):
    def wrap(request, *args, **kwargs):
        user=request.user
        if user.is_agent:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'you must be an agent')
            return render(request, "backpacker/login.html")
    return wrap


def customer_only(view_func):
    def wrap(request, *args, **kwargs):
        user=request.user
        if user.is_customer:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'you must be an User')
            return render(request, "backpacker/login.html")
    return wrap