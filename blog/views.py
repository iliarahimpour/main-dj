from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.views.generic import TemplateView
# Create your views here.


def post_list(request):
    post = Post.objects.order_by("-published_date")
    return render(request, 'blog/post_list.html', {"posts": post})


class HomePageView(TemplateView):
    template_name='blog/post_list.html'




class BlogPageView(TemplateView):
    template_name='blog/blog.html'




class BaseView(TemplateView):
    template_name='blog/base.html'