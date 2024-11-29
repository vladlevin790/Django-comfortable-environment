from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required 
from .forms import *
from .models import *
import json

def index(request, id=None):
    posts = Post.objects.all()
    posts_data = [{
        'title': post.title,
        'description': post.description,
        'photo_before': post.photo_before.name if post.photo_before else '',
        'photo_after': post.photo_after.name if post.photo_after else '',
        'cover': post.cover_photo.name if post.cover_photo else '',
        'latitude': post.latitude,
        'longitude': post.longitude,
    } for post in posts]

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
    else:
        form = QuestionForm()

    return render(request, 'index.html', {'posts_data': json.dumps(posts_data), 'posts': posts, 'form':form})

def commands(request):
    command = Command.objects.all()
    commands_data = {
        'commands' : command,
    }
    return render(request, 'our_commands.html', commands_data)

def posts(request):
    posts = Post.objects.all()
    posts_data = {
        'posts' : posts
    }
    return render(request, 'works.html', posts_data)


def about_us(request):
    return render(request, 'about_us.html')

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post' : post})

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
