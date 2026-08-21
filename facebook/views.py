from django.shortcuts import render
from .models import Post

def post_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})


