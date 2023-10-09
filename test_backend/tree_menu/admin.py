from django.contrib import admin


from .models import *


class MenuAdmin(admin.ModelAdmin):
    pass


class TopMenuItemAdmin(admin.ModelAdmin):
    exclude = ["parent"]


class NestedMenuItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Menu, MenuAdmin)
admin.site.register(TopMenuItem, TopMenuItemAdmin)
admin.site.register(NestedMenuItem, NestedMenuItemAdmin)

