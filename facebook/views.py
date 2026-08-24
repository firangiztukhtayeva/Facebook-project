from django.shortcuts import render, get_object_or_404
from .models import Post

def post_view(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'post/post_list.html', {'posts':posts})


def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post/post_detail.html", {'post': post})
    


