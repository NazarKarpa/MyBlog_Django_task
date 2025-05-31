from django.urls import path

import blog.views as blog_views

urlpatterns = [
    path("", blog_views.post_list, name='posts_list'),
    path('post-page/<int:post_id>', blog_views.page_post, name='page_post')
]