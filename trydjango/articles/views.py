from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Article
from .forms import ArticleForm

class ArticleList(ListView):
    queryset = Article.objects.all()
    template_name = 'articles/list.html'
    context_object_name = 'article'
    
class ArticleDetail(DetailView):
    queryset = Article.objects.all()
    template_name = 'articles/detail.html'
    context_object_name = 'article'   
    
    def get_object(self):
         id_ = self.kwargs.get('id')
         return get_object_or_404(Article, id=id_)
     
     
     
    
class ArticleCreate(CreateView):
    template_name = 'articles/create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    
    
    
    def form_invalid(self, form):
            print(form.cleaned_data)
            return super().form_invalid(form)
 
    
class ArticleUpdate(UpdateView):
    template_name = 'articles/update.html'
    form_class = ArticleForm
    
     
      
    def get_object(self):
         id_ = self.kwargs.get('id')
         return get_object_or_404(Article, id=id_)
     
     
class ArticleDelete(DeleteView):
    template_name = 'articles/delete.html'
    context_object_name = 'obj' 
    
    def get_success_url(self):
        return reverse('articles:create')
      
      
    def get_object(self):
         id_ = self.kwargs.get('id')
         return get_object_or_404(Article, id=id_)    

  