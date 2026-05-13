from django.shortcuts import render
from .models import Article

def articles_list(request):
    articles = Article.objects.all()  # Убираем prefetch_related
    return render(request, 'news/articles.html', {'object_list': articles})