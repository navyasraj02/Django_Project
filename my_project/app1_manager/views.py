from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('app1_manager:posts')
    else:
        form = PostForm()

    # Render either the form or the login template, depending on the request method
    if not request.user.is_authenticated:
        return render(request, 'app1_manager/login.html', {})
    return render(request, 'app1_manager/create_post.html', {'form': form})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'app1_manager/posts.html', {'posts': posts})
