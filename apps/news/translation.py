from modeltranslation.translator import  TranslationOptions,register
from .models import *

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description','category')
