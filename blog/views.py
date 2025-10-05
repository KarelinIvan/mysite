from urllib import request

from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    """Для просмотра списка опубликованных статей"""
    model = Post
    template_name = 'blog/post/post_list.html'
    context_object_name = 'posts'
    queryset = Post.published.all()  # Выводит к просмотру только статьи со статусом опубликовано
    paginate_by = 5


class PostDetailView(DetailView):
    """ДЛя просмотра детальной информации"""
    model = Post
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'
