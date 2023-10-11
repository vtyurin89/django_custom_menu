from django.contrib import admin

from .models import *
from .forms import *


class MenuAdmin(admin.ModelAdmin):
    pass


class TopMenuItemAdmin(admin.ModelAdmin):
    exclude = ["parent", "level"]
    ordering = ('menu', 'title')


class NestedMenuItemAdmin(admin.ModelAdmin):
    form = NestedMenuItemForm
    ordering = ('menu', 'title')
    exclude = ["level"]


admin.site.register(Menu, MenuAdmin)
admin.site.register(TopMenuItem, TopMenuItemAdmin)
admin.site.register(NestedMenuItem, NestedMenuItemAdmin)

