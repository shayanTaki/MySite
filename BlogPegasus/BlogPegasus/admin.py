from django import forms
from django.forms import Textarea
from .models import TexTak, menuItem
from django.contrib import admin

class TexTakForm(forms.ModelForm):
    class Meta:
        model = TexTak
        fields = '__all__'
        widgets = {
            'mtn1': Textarea(attrs={'style': 'width: 400px; height: 200px; font-size: 4vh; writing-mode: vertical-lr; text-orientation: mixed; unicode-bidi: bidi-override; direction: rtl; line-break: normal'}),
            'mtn2': Textarea(attrs={'style': 'width: 400px; height: 200px; font-size: 4vh; writing-mode: vertical-lr; text-orientation: mixed; unicode-bidi: bidi-override; direction: rtl; line-break: normal'}),
            'mtn3': Textarea(attrs={'style': 'width: 400px; height: 200px; font-size: 4vh; writing-mode: vertical-lr; text-orientation: mixed; unicode-bidi: bidi-override; direction: rtl; line-break: normal'}),
        }

class TexTakAdmin(admin.ModelAdmin):
    list_display = ['mtn1', 'mtn2', 'mtn3']
    form = TexTakForm

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'ویرایش مدل'
        extra_context['is_edit'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


class menuItemForm(forms.ModelForm):
    class Meta:
        model = menuItem
        fields = '__all__'



class menuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'mtn_kol', 'lnk_a']
    form = TexTakForm

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'ویرایش مدل'
        extra_context['is_edit'] = True
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


admin.site.register(TexTak, TexTakAdmin)
admin.site.register(menuItem, menuItemAdmin)
