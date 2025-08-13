from django.shortcuts import render
from django.views.generic import ListView ,CreateView,DetailView ,DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
 
class BlogsView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'blogs.html'
    context_object_name = 'posts'
class CreatePostView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'post_new.html'    
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user    
        return super().form_valid(form)

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'post'
class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'delete_post.html'
    success_url = reverse_lazy('article_list')
    context_object_name = 'post'