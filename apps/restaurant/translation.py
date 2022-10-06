from modeltranslation.translator import  TranslationOptions,register
from .models import *


@register(Restuarant)
class RestuarantTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CategoryMenu)
class CategoryMenuTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'description','category')