from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import BlogPost


def index(request):
    posts = BlogPost.objects.order_by('-date').filter(is_published=True)


    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts
    }

    return render(request, 'blog/index.html', context)



def post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'blog/post.html', context)