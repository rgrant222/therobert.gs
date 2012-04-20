# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import json

def default(request):
  people = ['Rob', 'Bob']

  questions = [
      {
        'question': 'What is your name?',
        'answers': {
          'Rob': 'Robert Grant',
          'Bob': 'Robert Graham',
        },
      },
      {
      'question': 'How old are you?',
      'answers': {
        'Rob': '28',
        'Bob': '27',
        },
      },
      {
      'question': 'Where were you born?',
      'answers': {
        'Rob': 'Bristol, England',
        'Bob': 'Lawrenceville, Georgia',
        },
      },
      {
      'question': 'How old were you when you used a computer for the first time?',
      'answers': {
        'Rob': ('I was 6!  It was 1992, and the computer (which cost a fortune,',
                'by the way) was a 386 DX clocked at a blazing 33Mhz!!'),
        'Bob': "Uh, ask me later... I can't seem to recall...",
        },
      },
  ]

  c = {
    'people': people,
    'questions': questions,
  }


  return render_to_response('aboutus.html', c,
                            context_instance=RequestContext(request))


def data(request):
  rob_profile = {
    'name': 'Rob',
    'age': 28,
    'city': 'Dacula',
    'state': 'Georgia',
    'picture': 'rob-profile.png',
  }

  data = []
  for n in range(10):
    data.append({
      'question': 'Title of Section %d' % n,
      'content': 'Here is the content of %d' % n,
    })
  
  return HttpResponse(json.dumps({'sections': data}, indent=2, default=str),
                      content_type="application/json") 
