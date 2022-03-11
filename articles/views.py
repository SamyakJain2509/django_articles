from django.shortcuts import render, redirect
from .models import Article
from .forms import PublishArticleForm
from users.models import Profile

def home(request):
    articles = Article.objects.all()

    return render(request, 'articles/index.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    profile = Profile.objects.get(user=article.author)    
    
    return render(request, 'articles/detail.html', {'article': article})

def publish(request):
    form = PublishArticleForm()
    if request.method == 'POST':
        form = PublishArticleForm(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.save()
            return redirect('home')
    return render(request, 'articles/create.html', {'form': form})