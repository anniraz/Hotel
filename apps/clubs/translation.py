from modeltranslation.translator import  TranslationOptions,register
from .models import *


@register(ClubsInfo)
class ClubsInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Clubs)
class ClubsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(SpaEtiquette)
class SpaEtiquetteTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
