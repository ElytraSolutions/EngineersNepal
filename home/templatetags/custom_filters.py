from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
def split_paragraphs(value):
    paragraphs = value.split('<p>')
    return paragraphs

@register.filter
def index(sequence, position):
    return sequence[position]


@register.simple_tag
def set(val=None):
  return val

@register.filter
@stringfilter
def upto(value, delimiter=None):
   return value.split(delimiter)[0]
upto.is_safe=True


