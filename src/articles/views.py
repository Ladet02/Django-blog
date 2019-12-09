from django.shortcuts import render
from .models import Article


def index(request):
    queryset = Article.objects.order_by('-timestamp')[:3]
    context = {
        'object_list': queryset
    }

    return render(request, 'index.html', context)


def article(request):
    return render(request, 'article.html', {})


def articles(request):
    return render(request, 'articles.html', {})


def about(request):
    return render(request, 'about.html', {})


def search(request):
    return render(request, 'search.html', {})
