__author__ = 'rob'

from django import template

register = template.Library()

@register.filter(name="lookup")
def lookup(d, k, f=""):
  try:
    return d.get(k, f)
  except Exception:
    return ""

@register.filter(name="index")
def index(d, i):
  try:
    return d[i]
  except Exception:
    return ""
