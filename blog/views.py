from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
  {
    'author': 'AlejandroC',
    'title': 'Blog Post 1',
    'content': 'first post content',
    'date_posted': 'August 27, 2021'
  },
  {
      'author': 'JulieBerta',
      'title': 'Blog Post 2',
      'content': 'second post content',
      'date_posted': 'August 28, 2021'
  },
]
def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
