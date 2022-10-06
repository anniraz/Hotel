from modeltranslation.translator import  TranslationOptions,register
from .models import *

# AboutHotel
# HotelFacilities,,

@register(Rooms)
class RoomTranslationOptions(TranslationOptions):
    fields = ('room', 'description',)