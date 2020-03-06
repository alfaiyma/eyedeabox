from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic

from TweetConnector import DataRefresh
from .models import TweetRef

import os

class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'tweet_list'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_queryset(self):
        return TweetRef.objects.all().order_by('-tweet_date')[:20]
    
def onDBRefresh(request: HttpRequest) -> HttpResponse:
    refreshAPi = DataRefresh.DataRefresh()
    refreshAPi.refresh()
    return HttpResponseRedirect(reverse('homepage:index'))


def aboutView(request: HttpRequest) -> HttpResponse:
    file_content: str = 'Error loading content'
    print(os.getcwd())
    with open('./homepage/Content/About.txt', 'r') as f:
        file_content = f.read()

    context = {
        'headline': "About",
        'content': file_content
    }
    return render(request, 'homepage/genericArticle.html', context)

def contactView(request: HttpRequest) -> HttpResponse:
    context = {
        'headline': "Contact Details",
        'content': "Ideas, suggestions or comments? Email me at eyedeabox@mohammad-alfaiyaz.com"
    }
    return render(request, 'homepage/genericArticle.html', context)