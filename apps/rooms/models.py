from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from apps.home.models import PhotoGallery

class Amenities(models.Model):

    title=models.CharField(max_length=50)   
    amenitiesIcon=models.ImageField(upload_to='icons/')

    def __str__(self):
        return f'{self.title}'


class Rooms(models.Model):
    
    HOTEL_CHOICES=(
        ('Junior Suite','Junior Suite'),
        ('Family Room','Family Room'),
        ('Double Room','Double Room'),
        ('Deluxe Room','Deluxe Room'),
        ('Superior Room','Superior Room'),
        )
        
    ROOM_CHOICE=(
        (1,1),
        (2,2),
        (3,3),
        (4,4),
    )
    room_number=models.PositiveIntegerField(unique=True)
    room=models.CharField(max_length=100,choices=HOTEL_CHOICES)
    is_available=models.BooleanField(default=True)
    photo=models.ImageField(upload_to='rooms/')
    price=models.PositiveIntegerField()
    for_persons=models.PositiveIntegerField()
    for_children=models.PositiveIntegerField(default=0)
    room_amount=models.PositiveIntegerField(choices=ROOM_CHOICE,default=1)
    description=RichTextUploadingField()

    def __str__(self):
        return f'Room number:{self.room_number}  {self.room} '
    

    # def save(self,*args,**kwargs):
    #     if self.photo:
    #         a=PhotoGallery.objects.create(image=self.photo)


    #     return super().save(*args,**kwargs)









