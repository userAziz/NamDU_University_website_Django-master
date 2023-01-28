from django.shortcuts import render,redirect
from lost_found.models import lost_found
from django.contrib.auth.decorators import login_required


def contact(request):
	return render(request, 'contact.html')