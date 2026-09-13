from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article, Comment


def article_list(request):
    articles = Article.objects.all()
    page_obj = Paginator(articles, 6).get_page(request.GET.get('page'))
    context = {'articles': page_obj, 'page_obj': page_obj, 'paginator': page_obj.paginator}
    return render(request, 'article/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article/article_detail.html', {'article': article})


def add_comment(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if not request.user.is_authenticated:
        return redirect('login_page')

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        if text:
            Comment.objects.create(article=article, user=request.user, text=text)

    return redirect(article.get_absolute_url() + '#comments')
