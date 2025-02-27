from django import template
from ..models import CentreProfile

register = template.Library()

@register.simple_tag
def get_masjid():
    return CentreProfile.objects.get(pk=1)