from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(
    "<center><b><h2>I hope today they will give my salary. \
    Otherwise I will not have any motivation :( <h2></b></center>"
    )