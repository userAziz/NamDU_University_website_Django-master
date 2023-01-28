from django.shortcuts import render,redirect
from lost_found.models import lost_found
from django.contrib.auth.decorators import login_required

# Create your views here.from article_app.models import Article
# Create your views here.
def item_list(request):
	items_from_database = lost_found.objects.all().order_by('date')
	return render(request, 'lost_found.html', {'items_from_database':items_from_database})
# def main_page(request):
# 	return render(request, 'index.html')

# def item_details(request, slug_path):
# 	item_article = lost_found.objects.get(slug_path = slug_path)
# 	return render(request, 'lost_found_items.html', {'item_article':item_article})