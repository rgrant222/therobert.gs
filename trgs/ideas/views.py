# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def default(request):
	c = {}
	return render_to_response('ideas.html', c, context_instance=RequestContext(request))