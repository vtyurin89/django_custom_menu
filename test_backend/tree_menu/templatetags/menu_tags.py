from django import template

from ..models import *

register = template.Library()


@register.inclusion_tag('tree_menu/menu_template.html')
def draw_menu():
    return 0

