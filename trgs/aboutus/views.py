# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import json

def default(request):
  return render_to_response('aboutus.html',
                            {},
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
