from django import forms
from django.contrib import admin

from .models import NestedMenuItem, MenuItem


class NestedMenuItemForm(forms.ModelForm):
    class Meta:
        model = NestedMenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NestedMenuItemForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = MenuItem.objects.all().order_by('menu', 'level', '-id')
