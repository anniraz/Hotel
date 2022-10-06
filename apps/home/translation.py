from modeltranslation.translator import  TranslationOptions,register
from .models import *

# AboutHotel
# HotelFacilities,,

@register(AboutHotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('title', 'description','address')

@register(HotelFacilities)
class HotelFacilitiesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ExtraServicesPoints)
class ExtraServicesPointsTranslationOptions(TranslationOptions):
    fields = ('points', )

@register(ExtraServicesInfo)
class ExtraServicesInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')