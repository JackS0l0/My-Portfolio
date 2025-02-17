from django.contrib import admin
from .models import Articles,Categories
from modeltranslation.admin import TranslationAdmin
@admin.register(Categories)
class CategoriesControl(TranslationAdmin):
    group_fieldsets = True  
    list_display=['name','id']
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(Articles)
class ArticlesControl(TranslationAdmin):
    group_fieldsets = True  
    list_display=['name','cate','sale','complated']
    search_fields=['name','id']
    list_filter=['cate','date']
    fields=['name','cate','img','date','slug','advertTrendTxt','desc','sale','complated']
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }