# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

def home(request):
    menu_items = [    
        {
            'text': "Bob's", 
            'href': '/'
        },
        {
            'text': "Rob's", 
            'href': '/'
        },
        {
            'text': 'Ideas', 
            'href': '/'
        },
        {
            'text': 'About Us', 
            'href': '/aboutus/'
        }
    ]

    t = loader.get_template('home.html')
    c = Context({'menu_items': menu_items})
    return HttpResponse(t.render(c))
