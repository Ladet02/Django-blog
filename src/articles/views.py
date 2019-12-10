from django.shortcuts import render
from .models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q


def search(request):
    queryset = Article.objects.order_by('-timestamp')

    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(
                overview__icontains=query)
        ).distinct()

    paginator = Paginator(queryset, 10)
    page_request_variable = 'page'
    page_number = request.GET.get(page_request_variable)

    try:
        paginated_queryset = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'search_results': queryset,
        'page_request_variable': page_request_variable
    }
    return render(request, 'search.html', context)


def index(request):
    queryset = Article.objects.order_by('-timestamp')[:3]
    context = {
        'object_list': queryset
    }

    return render(request, 'index.html', context)


def article(request, id):
    return render(request, 'article.html', {})


def about(request):
    return render(request, 'about.html', {})


def browse(request):
    article_list = Article.objects.order_by('-timestamp')

    paginator = Paginator(article_list, 5)
    page_request_variable = 'page'
    page_number = request.GET.get(page_request_variable)

    try:
        paginated_queryset = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'article_list': paginated_queryset,
        'page_request_variable': page_request_variable
    }
    return render(request, 'browse.html', context)
