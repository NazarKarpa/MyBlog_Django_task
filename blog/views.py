from django.shortcuts import render

from blog.models import Blog

def post_list(request):
    post = Blog.objects.all()
    context = {
        'posts_list': post,

    }
    return render(
        request,
        'blog/post_list.html',
        context=context,
    )

def page_post(request, post_id):
    post = Blog.objects.get(id = post_id)

    context = {
        'post': post,

    }
    return render(
        request,
        'blog/page_post.html',
        context=context,
    )


