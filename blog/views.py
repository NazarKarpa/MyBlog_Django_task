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
