from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        "message": "Welcome to My Blog",
        "description": "This is my blog.",
        "articles": articles
    }
    return render(request, "blog/index.html", context)

def detail(request, id):
    article = Article.objects.get(pk=id)
    context = {
        "article": article,
    }
    return render(request, "blog/detail.html", context)

def create(request):
    article = Article(title="Article1", content="texttexttexttexttexttexttexttexttexttexttext")
    article.save()

    articles = Article.objects.all()
    context = {
        "message": "Welcome to My Blog",
        "description": "This is my blog.",
        "articles": articles
    }
    return render(request, "blog/index.html", context)