from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def article(request):
    return render(request, 'article.html', {})


def articles(request):
    return render(request, 'articles.html', {})


def about(request):
    return render(request, 'about.html', {})
