from django import template

register = template.Library()

@register.filter
def clean_trait(value):
    return value.replace('_', ' ').title()