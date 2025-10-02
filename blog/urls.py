from blog.views import PostListView, PostDetailView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
]
