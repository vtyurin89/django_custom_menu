from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max, Count

from ..models import *

register = template.Library()


@register.inclusion_tag('tree_menu/menu_template.html',  takes_context=True)
def draw_menu(context, menu_title):
    root_items = MenuItem.objects.filter(
        menu__title=menu_title, parent=None
    ).prefetch_related('children')
    return {
        'root_items': root_items,
        'request': context['request'],
    }
