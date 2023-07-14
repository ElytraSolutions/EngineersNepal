from django import template

register = template.Library()

@register.filter
def split_paragraphs(value):
    paragraphs = value.split('<p>')
    return paragraphs

@register.filter
def index(sequence, position):
    return sequence[position]
