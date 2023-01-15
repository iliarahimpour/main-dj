from django.urls import path
from . import views
from .views import HomePageView , BlogPageView , BaseView

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', BaseView.as_view(), name='base'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('home', HomePageView.as_view(), name='home'),
]

