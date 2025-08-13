from django.urls import path
from .views import BlogsView ,CreatePostView ,ArticleDetailView ,ArticleDeleteView

urlpatterns = [
    path('',BlogsView.as_view(),name='article_list'),
    path('addnewpost/',CreatePostView.as_view(),name='create_post'),
    path('article_lists/<int:pk>/',ArticleDetailView.as_view(),name='article_detail'),
    path('article_lists/<int:pk>/delete/',ArticleDeleteView.as_view(),name='delete_post')
]
