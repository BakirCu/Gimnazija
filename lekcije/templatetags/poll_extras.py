from django import template

register = template.Library()


@register.filter
def extension(value):
    extension = str(value).split('.')[-1]
    return extension
