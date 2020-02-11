from django.shortcuts import render, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import generic

from TweetConnector import DataRefresh
from .models import TweetRef

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
    context = {
        'headline': "About",
        'content': "Hello everyone and thank you for visting this little app. What is this app about? Well it's to provide you a look into what needs that are not being met. I hope this site inspires you to go on a journey to bring an idea to life."
    }
    return render(request, 'homepage/genericArticle.html', context)

def contactView(request: HttpRequest) -> HttpResponse:
    context = {
        'headline': "Contact Details",
        'content': "Email: eyedeabox@mohammad-alfaiyaz.com\n" 
    }
    return render(request, 'homepage/genericArticle.html', context)