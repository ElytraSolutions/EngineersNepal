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
    parts = value.split(delimiter)
    print(parts)
    if len(parts) == 2:  # If there are two parts (hours and minutes)
        return parts[0]
    elif len(parts) == 1:  # If there's only one part (minutes or hours)
        if delimiter == ",":
            return parts[0]
        else:
            return parts[0]
    
    return value  # If the input format is not recognized
upto.is_safe=True


