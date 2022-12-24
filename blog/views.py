from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'index.html', {"articles": articles})

def article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {'article': article})

def modify_article(request, id):   
    article = get_object_or_404(Article, id=id)
   
    formulaire = ArticleForm(initial={'title':article.title, 'content':article.content})
    formulaire.__setattr__('class', 'form-post')
    
    return render(request, 'edit.html', {'formulaire': formulaire, 'article':article})


def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
           
            article.title = cd['title']
            article.content = cd['content']
            article.save()
            return render(request, 'succes.html')
        else:
            return render(request, 'error.html', {'message': 'erreur de soumission du formulaire'})
    else:
        return render(request, 'error.html', {'message': 'Method not allowed'})





