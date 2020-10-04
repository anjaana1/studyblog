from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import PostForm


def index(request):
    data = {
        'post_list': Post.objects.all().order_by("-post_id"),
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)


def search(request):
    if request.method == "GET" and request.GET.get('search') != "":
        search = request.GET.get('search')
        condition = Q(post_title__contains=search) | Q(post_desc__contains=search)
        posts = Post.objects.filter(condition)
        return render(request, 'index.html', context={'post_list': posts,'categories':Category.objects.all()})


def category(request,cat_id):
    categories = Category.objects.get(cat_id=cat_id)
    data = {
        'post_list': Post.objects.filter(post_category=categories),
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', data)


def add_post(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(add_post)
    categories = Category.objects.all()
    data = {
        'categories': categories,
        'posts': Post.objects.all().order_by('-post_id'),
        'form': form
    }

    return render(request, 'add_post.html', data)


def update_post(request, post_id):
    if request.method == "POST":
        get_post = Post.objects.get(post_id=post_id)
        form = PostForm(request.POST or None, instance=get_post)
        if form.is_valid():
            form.save()
            return redirect(update_post)
    else:
        get_post = Post.objects.get(post_id=post_id)
        form = PostForm(request.POST or None, instance=get_post)
    return render(request, 'update_post.html', {'form': form})


def view_post(request, post_id):
    return render(request, 'view_post.html', {'posts': Post.objects.get(post_id=post_id)})


def delete_post(request, post_id):
    get_post = Post.objects.get(post_id=post_id)
    get_post.delete()
    return redirect(add_post)
