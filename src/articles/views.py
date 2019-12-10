from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core.exceptions import DoesNotExist

from django.db.models import Q

from .forms import CommentForm


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
    article = get_object_or_404(Article, id=id)

    # Try to get the next & previous articles, based on id (possible since our id's are all consecutive integers —> would break if we deleted even one article!!)
    try:
        next_article = Article.objects.get(id=(str(int(id) + 1)))
    except Article.DoesNotExist:
        next_article = None

    try:
        previous_article = Article.objects.get(id=(str(int(id) - 1)))
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
                'id': article.id,
            }))

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
