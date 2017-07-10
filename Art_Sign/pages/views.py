import datetime

from django.shortcuts import render

from Art_Sign.agenda.models import Event
from Art_Sign.article.models import Article


def home(request):
    today = datetime.date.today()
    events = Event.objects.order_by('-date').filter(date__gte=today)
    articles = Article.objects.order_by('-pub_date') \
        .exclude(pub_date__gte=today)

    return render(request, 'pages/home.html', {
        'next_events': events,
        'last_articles': articles,
    })


def about(request):
    return render(request, 'pages/about.html')


def achievements(request):
    today = datetime.date.today()
    articles = Article.objects.filter(category=1) \
        .exclude(pub_date__gte=today) \
        .order_by('-pub_date')

    return render(request, 'pages/achievements.html', {
        'articles': articles,
    })


def services(request):
    today = datetime.date.today()
    articles = Article.objects.filter(category=2) \
        .exclude(pub_date__gte=today) \
        .order_by('-pub_date')

    return render(request, 'pages/services.html', {
        'articles': articles,
    })


def outings(request):
    today = datetime.date.today()
    articles = Article.objects.filter(category=3) \
        .exclude(pub_date__gte=today) \
        .order_by('-pub_date')

    return render(request, 'pages/outings.html', {
        'articles': articles,
    })


def participate(request):
    return render(request, 'pages/participate.html')
