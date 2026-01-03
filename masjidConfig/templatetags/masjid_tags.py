from django import template
from ..models import CentreProfile

register = template.Library()

@register.simple_tag
def get_masjid():
    return CentreProfile.objects.get(pk=1)

@register.filter
def get_item(dictionary, key):
    """Get item from dictionary using a key"""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None