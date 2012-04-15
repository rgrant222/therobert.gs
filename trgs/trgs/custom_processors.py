def main_nav(request):
    menu_items = [    
        {
            'text': "Bob's", 
            'href': '/bob/'
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

    return {'menu_items': menu_items}

