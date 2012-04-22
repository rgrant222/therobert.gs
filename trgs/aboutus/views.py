# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response


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
        'Bob': 'Mesquite, Texas',
        },
      },
      {
      'question': 'How old were you when you used a computer for the first time?',
      'answers': {
        'Rob': 'I was 6!  It was 1992, and the computer (which cost a fortune, by the way) was a 386 DX clocked at a blazing 33Mhz!!',
        'Bob': "Dad tells me I was 3 years old using a computer of his at work learning my shapes from a program he had written FORTRAN. I don't remember this, but I guess I've never had any problems identifying shapes...",
        },
      },
  ]

  c = {
    'people': people,
    'questions': questions,
  }


  return render_to_response('aboutus.html', c,
                            context_instance=RequestContext(request))