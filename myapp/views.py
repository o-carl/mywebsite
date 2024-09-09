from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})

def homepage(request):
    return render(request, 'homepage.html')