from django import template
from django.urls import reverse, get_script_prefix, NoReverseMatch
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max, Count

from ..models import *

register = template.Library()


@register.inclusion_tag('tree_menu/menu_template.html',  takes_context=True)
def draw_menu(context, menu_title):
    menu_items = MenuItem.objects.filter(menu__title=menu_title).select_related('parent')
    for item in menu_items:
        try:
            item.url = reverse(item.url)
        except NoReverseMatch:
            pass
        if item.parent and item.parent.url == context['request'].path:
            item.nested_menu = True

        item.nested_children_list = getattr(item, 'nested_children_list', [])
        if item.parent:
            item.parent.nested_children_list = getattr(item.parent, 'nested_children_list', [])
            item.parent.nested_children_list += [item]
    for item in menu_items:
        print(item.nested_children_list)
    return {
        'menu_items': menu_items,
        'request': context['request'],
    }
