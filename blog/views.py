from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    # The request parameter is parameter required by all the views
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    # get_object_or_404, retives the desired object from the Post model and returns a HTTP 404 error, if no such object is found
    return render(request, 'blog/post/detail.html', {'post': post})