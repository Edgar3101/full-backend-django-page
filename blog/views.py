from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Profile
from django.template import loader

def home(request):
    post_list = Post.objects.order_by('-created_on')[:5]
    template = loader.get_template('blog/home.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))
def post_views(request):
    post_list = Post.objects.order_by('-created_on')[:5]
    template = loader.get_template('blog/post_views.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))
def profile(request):
    profile_list = Profile.objects.order_by('-update_on')[:5]
    template = loader.get_template('blog/profile.html')
    context = {
        'profile_list': profile_list,
    }
    return HttpResponse(template.render(context, request))
def contacts(request):
    post_list = Post.objects.order_by('-created_on')[:5]
    template = loader.get_template('blog/contacts.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))
def resume(request):
    post_list = Post.objects.order_by('-created_on')[:5]
    template = loader.get_template('blog/resume.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))
    
# Create your views here.
