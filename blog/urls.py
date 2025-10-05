from blog.views import PostListView, PostDetailView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
