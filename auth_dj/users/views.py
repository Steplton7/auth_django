from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def login(request):
    return render(request, 'users/login.html')
    #return HttpResponse("<h2>О сайте!</h2>")

