from django.shortcuts import redirect, render
from .models import PostForm, Post
# Create your views here.


def Home(request):

    post = Post.objects.all().order_by("-updated")

    context = {
        "title": "home",
        "post": post
    }
    return render(request, 'home.html', context)


def Create(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    form = PostForm()

    context = {
        "title": "create",
        "form": form
    }
    return render(request, 'create.html', context)


def Update(request, pk):
    post = Post.objects.get(id=pk)
    # print(request.POST)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('update', pk)

    form = PostForm(instance=post)

    context = {
        "title": "update",
        "form": form
    }
    return render(request, "update.html", context)

def Delete(request, pk):
    post = Post.objects.get(id=pk)
    print(pk)
    print("delete")
    print(request.POST)

    if request.method == "POST":
        print(post)
        post.delete()

        
        return redirect("home")

    context = {
        "title": "home",
        "post": post
    }
    return render(request, "home.html", context)

