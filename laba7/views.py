from django.shortcuts import render, render_to_response
from django.contrib import auth

# Create your views here
def home(request):
    if str(auth.get_user(request)) == "AnonymousUser":
        userna= None
    else:
        userna = auth.get_user(request)

    return render_to_response('base.html', {"username": userna})
