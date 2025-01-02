"""
URL configuration for Diplom_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, re_path
from blog.views import posts, details, delete_post, after_delete, new_post, new_post_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts, name='home'),
    re_path(r'^posts/(?P<slug>[-a-zA-Z0-9а-яА-ЯёЁ]+)/$', details, name='details'),
    re_path(r'^posts/(?P<slug>[-a-zA-Z0-9а-яА-ЯёЁ]+)/delete/$', delete_post, name='post_delete'),
    path('posts/deleted/<str:title>/', after_delete, name='after_delete'),
    path('new/', new_post_form, name='new_post_form'),
    path('new/submit/', new_post, name='new_post')
]

