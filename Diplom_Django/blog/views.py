from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
import re
from blog.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def all_posts(request):
    posts_list = Post.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts_list})


def get_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'details.html', {'post': post})


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
    return redirect('/home_page')


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


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        title = post.title
        post.delete()
        return redirect('after_delete', title=title)
    return render(request, 'post_detail.html', {'post': post})


def after_delete(request, title):
    return render(request, 'after_delete.html', {'title': title})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def _login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')
