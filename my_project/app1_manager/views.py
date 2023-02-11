from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('app1_manager:index')
    else:
        form = PostForm()
    return render(request, 'app1_manager/create_post.html', {'form': form})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'app1_manager/posts.html', {'posts': posts})
