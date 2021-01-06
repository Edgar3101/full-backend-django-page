from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')
def post_views(request):
    return render(request, 'blog/post_views.html')
def profile(request):
    return render(request, 'blog/profile.html')
def contacts(request):
    return render(request, 'blog/contacts.html')
def resume(request):
    return render(request, 'blog.resume.html')
# Create your views here.
