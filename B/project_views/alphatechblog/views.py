from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'alphatechblog/home.html', {})

def blog(request):
    return render(request, 'alphatechblog/blog.html', {})

def mentor(request):
    return render(request, 'alphatechblog/mentor.html', {})

def mentee(request):
    return render(request, 'alphatechblog/mentee.html', {})

def author(request):
    return render(request, 'alphatechblog/author.html', {})


