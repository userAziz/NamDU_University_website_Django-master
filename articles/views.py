from django.shortcuts import render,redirect
from articles.models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.from article_app.models import Article
# Create your views here.
def article_list(request):
	articles_from_database = Article.objects.all().order_by('date')
	return render(request, 'article.html', {'articles_from_database':articles_from_database})
# def main_page(request):
# 	return render(request, 'index.html')

def article_details(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'each_article.html', {'article':article})

@login_required(login_url='/log_in/')
def article_create(request):
	if request.method =='POST':
		form=forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit='False')
			instance.author = request.user
			instance.save()
			return redirect('items:list_of_items')
	else:
	    form =forms.CreateArticle()
	return render(request, 'article_create.html', {'form':form})

def index(request):
	articles_from_database = Article.objects.all().order_by('date')
	return render(request, 'index.html', {'articles_from_database':articles_from_database})

def our_team(request):
    return render(request, 'our_team.html')

def majors(request):
    return render(request, 'majors.html')


def admissions(request):
    return render(request, 'admissions.html')

def campus(request):
    return render(request, 'campus.html')