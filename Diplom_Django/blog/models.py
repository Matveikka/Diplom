from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()
    rezume = models.TextField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            if self.title:
                base_slug = slugify(self.title)
                slug = base_slug
                counter = 1
                while Post.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                self.slug = slug
                print(f"Generated slug: {self.slug}")
            else:
                print("Title is empty; cannot generate slug.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
