from django.shortcuts import render
from django.http import HttpResponse


def homeView(request, template_name='base.html'):
	return render(request, template_name)


def blogSinglesidebar(request, template_name='blog-single-sidebar.html'):
	return render(request, template_name)


def blogGridsidebar(request):
	template_name = 'blog-grid-sidebar.html'
	return render(request, template_name)

def blogSingle(request):
	template_name = 'blog-single.html'
	return render(request, template_name)

def contactView(request):
	template_name = 'contact.html'
	return render(request, template_name)