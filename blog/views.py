from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

# Create your views here.

class StartingPageView(ListView):
    pass

class AllPostsView(ListView):
    pass

class SinglePostView(View):
    pass

class ReadLaterView(View):
    pass