from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Status  # αν χρειαστεί
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.filter(status=Status.PUBLISHED)
    paginator = Paginator(post_list, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
