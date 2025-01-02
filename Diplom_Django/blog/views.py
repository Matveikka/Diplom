from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from blog.models import Post
import re


# Create your views here.
def posts(request):
    posts_list = Post.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts_list})


def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'details.html', {'post': post})


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        title = post.title
        post.delete()
        return redirect('after_delete', title=title)

    return render(request, 'post_detail.html', {'post': post})


def after_delete(request, title):
    return render(request, 'after_delete.html', {'title': title})


def generate_slug(title):
    slug = re.sub(r'[^a-zA-Zа-яА-Я0-9-]', '-', title.lower())
    slug = re.sub(r'-+', '-', slug).strip('-')
    original_slug = slug
    count = Post.objects.filter(slug=slug).count()
    i = 1
    while count > 0:
        slug = f"{original_slug}-{i}"
        count = Post.objects.filter(slug=slug).count()
        i += 1
    return slug


def new_post_form(request):
    return render(request, 'add_post.html')


def new_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        rezume = request.POST['rezume']
        info = request.POST['info']
        slug = generate_slug(title)
        post = Post.objects.create(
            title=title,
            rezume=rezume,
            info=info,
            slug=slug)
        return redirect('/')
    return redirect('new_post')
