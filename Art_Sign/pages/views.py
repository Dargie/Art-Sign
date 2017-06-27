import datetime

from django.shortcuts import render

from Art_Sign.agenda.models import Event
from Art_Sign.article.models import Article


def home(request):
    today = datetime.date.today()
    events = Event.objects.order_by('-date').filter(date__gte=today)
    articles = Article.objects.order_by('-pub_date')

    return render(request, 'pages/home.html', {
        'next_events': events,
        'last_articles': articles,
    })


def about(request):
    return render(request, 'pages/about.html')