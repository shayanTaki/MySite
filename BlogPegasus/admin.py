from django.contrib import admin
from django.forms import Textarea
from .models import TexTak

@admin.register(TexTak)
class TexTakAdmin(admin.ModelAdmin):
    list_display = ['mtn1', 'mtn2']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['mtn1'].widget = Textarea(attrs={
            'style': 'width: 400px; height: 200px;font-size: 4vh; writing-mode: vertical-lr; text-orientation: mixed; unicode-bidi: bidi-override; direction: rtl; line-break: normal'
        })
        form.base_fields['mtn2'].widget = Textarea(attrs={
            'style': 'width: 400px;font-size: 4vh; height: 200px; writing-mode: vertical-lr; text-orientation: mixed; unicode-bidi: bidi-override; direction: rtl; line-break: normal'
        })
        return form
