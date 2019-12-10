from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

from tinymce.models import HTMLField


# Create your models here.

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="Anonymous")
    bio = models.TextField()
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30, default="Random")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    title = models.CharField(max_length=30, default="Random")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    timestamp = models.DateTimeField()
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    content = HTMLField('')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"id": self.id})

    @property
    def get_comments(self):
        # .order_by('-timestamp') # Add that after '.all()' If you want the newest comments on top
        return self.comments.all()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        # The reason we have this crazy interpolated string is for the comments section of the admin page
        # Here we have a fancy way to get the first five words of a comment
        return f'{self.user.username} ——— {self.article.title} ——— {(" ").join((self.content).split()[0:5])}...'
