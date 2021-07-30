from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class IndexPage(TemplateView):
  def get(self,request,**kwargs):
    article_data = []
    all_article_objs = Article.objects.all().order_by('-created_at')[:9]
    for article in all_article_objs:
      article_data.append({
        'title':article.title,
        'cover':article.cover.url,
        'created_at':article.created_at,
        'category': article.category
      })
    context = {'all_article_objs':all_article_objs}
    return render(request,'index.html',context)
