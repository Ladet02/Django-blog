from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

from tinymce.models import HTMLField

from django.template.defaultfilters import slugify
from datetime import datetime

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
    slug = models.SlugField(unique=True)

    overview = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    import_code_highlighting_styles = models.BooleanField(default=False)

    content = HTMLField('')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={'slug': self.slug})

    @property
    def get_comments(self):
        # .order_by('-timestamp') # Add that after '.all()' if you want the newest comments on top
        return self.comments.all()

    @property
    def get_reading_time(self):
        html_words_array = self.content.split(' ')

        def remove_html_tags(text):
            """Remove html tags from a string"""
            import re
            clean = re.compile(
                r'<.*?>|src="(.|\n)*?"|alt="(.|\n)*?"|width="(.|\n)*?"|height="(.|\n)*?"|href="(.|\n)*?"|class="(.|\n)*?"|id="(.|\n)*?"|style="(.|\n)*?"')
            return re.sub(clean, '', text)

        words = [remove_html_tags(word)
                 for word in html_words_array if 'jpg' not in word]

        # assuming people read at 250 words per minute
        words_per_minute = 175

        return int(len(words) / words_per_minute)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        # Here we have a fancy way to get the first five words of a comment
        return f'{(" ").join((self.content).split()[0:5])}...'
