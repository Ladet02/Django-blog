from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core.exceptions import DoesNotExist

from django.db.models import Q

from .forms import CommentForm


def search(request):
    queryset = Article.objects.order_by('-timestamp')

    # General search
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(
                overview__icontains=query) | Q(content__icontains=query) | Q(categories__title__icontains=query) | Q(tags__title__icontains=query)
        ).distinct()

    # Category search
    category_query = request.GET.get('category_q')
    if category_query:
        queryset = queryset.filter(
            Q(categories__title__icontains=category_query)
        ).distinct()

    # Tag search
    tag_query = request.GET.get('tag_q')
    if tag_query:
        queryset = queryset.filter(
            Q(tags__title__icontains=tag_query)
        ).distinct()

    # Search results pagination
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


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    # Try to get the next & previous articles, using Django's incredible "get_next_by_FOO" function!!
    try:
        next_article = article.get_next_by_timestamp()
    except Article.DoesNotExist:
        next_article = None

    try:
        previous_article = article.get_previous_by_timestamp()
    except Article.DoesNotExist:
        previous_article = None

    # Comment form
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.article = article
            form.save()
            return redirect(reverse("article-detail", kwargs={
                'slug': article.slug,
            }) + "#comments")

    context = {
        'article': article,
        'next_article': next_article,
        'previous_article': previous_article,
        'comment_form': form
    }
    return render(request, 'article.html', context)


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
