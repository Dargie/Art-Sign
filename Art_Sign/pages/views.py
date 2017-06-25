import datetime

from django.shortcuts import render

from Art_Sign.agenda.models import Event


def home(request):
    today = datetime.date.today()
    events = Event.objects.order_by('-date').filter(date__gte=today)

    return render(request, 'pages/home.html', {
        'next_events': events,
    })

