from modeltranslation.translator import TranslationOptions,register
from articles.models import Articles,Categories
@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ['name','desc','advertTrendTxt']
@register(Categories)
class CategoriesTranslationOptions(TranslationOptions):
    fields = ['name']