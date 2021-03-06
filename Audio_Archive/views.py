from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Conference, Talk

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def program(request):
    latest_conference = Conference.objects.order_by('-year')
    max_sessions_per_slot = 0
    for day in latest_conference[0].day_set.all():
        for timeslot in day.timeslot_set.all():
            if len(timeslot.talk_set.all()) > max_sessions_per_slot:
                max_sessions_per_slot = len(timeslot.talk_set.all())

    context = { 'latest_conference': latest_conference[0], 'max_sessions': max_sessions_per_slot}
    return render(request, 'program.html', context)

def talk(request, talk_id):
    talk = get_object_or_404(Talk, talk_id)
    return render(request, 'talk.html', {'talk': talk})