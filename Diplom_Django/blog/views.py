from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def posts(request):
    posts_list = Post.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts_list})


def details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'details.html', {'post': post})
