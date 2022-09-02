from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import requests
from .forms import contactform
# Create your views here.

def tech_news(request):
	url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'tech_news.html',context)

def sports_cricket(request):
	url = f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'sports_cricket.html',context)

def sports_football(request):
	url = f'https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'sports_football.html',context)

def sports_volleyball(request):
	url = f'https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'sports_volleyball.html',context)

def sports_hockey(request):
	url = f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'sports_hockey.html',context)


def general_news(request):
	url = f'https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'news.html',context)

def health(request):
	url = f'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'health.html',context)

def education(request):
	url = f'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=1a04b21ba9d9425f9f1d5d994d0f01c6'
	data = requests.get(url)
	response = data.json()
	articles = response['articles']
	context = {'articles':articles}
	return render(request,'education.html',context)

def about(request):
	return render(request,'about.html')

def feedback(request):
	form = contactform()
	if request.method == 'POST':
                form = contactform(request.POST)
                if form.is_valid():
                        form.save()
                        form = contactform()
	return render(request,'contact_form.html',{'form':form})


