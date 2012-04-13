# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

def default(request):
    t = loader.get_template('aboutus.html')
    return HttpResponse(t.render(Context()))
