from django import template

register = template.Library()

@register.filter
def split_paragraphs(value):
    paragraphs = value.split('<p>')
    return paragraphs
