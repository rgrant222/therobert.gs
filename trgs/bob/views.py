# Create your views here.
# Create your views here.

import django.template
from django.shortcuts import render_to_response
import django.http

def bob(request):
    """

    """
    return render_to_response('bob.html',
            {},
        context_instance=django.template.RequestContext(request))
