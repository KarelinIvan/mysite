from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    # Для просмотра списка опубликованных статей
    model = Post
    template_name = 'blog/post/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'
