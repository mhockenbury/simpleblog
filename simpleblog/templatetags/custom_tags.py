from django import template

register = template.Library()

@register.filter
def as_percentage(value):
    return format(value, ".2%")
