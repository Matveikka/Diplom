from django.db import models


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    title = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self):
        return self.title


