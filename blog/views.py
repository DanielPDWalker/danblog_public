from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import BlogPost
from .utils import get_string_list_of_formatted_tags


def index(request):
    posts = BlogPost.objects.order_by('-date').filter(is_published=True)
    tag_list = get_string_list_of_formatted_tags(posts)


    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        "posts": paged_posts,
        "tag_list": tag_list
    }

    return render(request, 'blog/index.html', context)



def post(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
    tag_list = get_string_list_of_formatted_tags(post)

    context = {
        "post": post,
        "tag_list": tag_list
    }

    return render(request, 'blog/post.html', context)


def tag (request):
    posts = BlogPost.objects.all()
    tag_list = get_string_list_of_formatted_tags(posts)

    context = {
        "tag_list": tag_list
    }
    return render(request, 'blog/tag.html', context=context)


def tag_search(request, tag_string):
    posts = BlogPost.objects.order_by('-date').filter(tags__contains=tag_string)
    tag_list = get_string_list_of_formatted_tags(posts)

    context = {
        "tag_string": tag_string,
        "tag_list": tag_list,
        "posts": posts
    }
    return render(request, 'blog/tag_search.html', context)
