from django.views.generic import ListView
from Diplom.blog.models import Blog


# Create your views here.
class ArticleListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blog'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(published=True).order_by('-published_date')
