# Create your views here.

from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
	c = {}
	c['happening_posts'] = pymongo.Connection()['trgs']['posts'].find().sort([('date', -1)]).limit(5)
	return render_to_response('home.html',
                              c,
                              context_instance=RequestContext(request))
