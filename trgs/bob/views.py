# Create your views here.
# Create your views here.

from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse

def bob(request):
    return render_to_response('bob.html',
            {},
        context_instance=RequestContext(request))
