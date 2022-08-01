from django.shortcuts import redirect, render
from .models import PostForm, Post
# Create your views here.


def Home(request):

    post = Post.objects.all()

    context = {
        "title": "home",
        "post": post
    }
    return render(request, 'home.html', context)


def Update(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    form = PostForm()

    context = {
        "title": "home",
        "form": form
    }
    return render(request, 'update.html', context)
