from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        mains = sum(1 for form in self.forms
                   if form.cleaned_data and form.cleaned_data.get('is_main'))
        if mains != 1:
            raise ValidationError('Должен быть ровно один основной тег!')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    fields = ['tag', 'is_main']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    inlines = [ScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['article', 'tag', 'is_main']