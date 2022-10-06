from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from apps.home.models import PhotoGallery,VideoGallery

# Create your models here.


class Restuarant(models.Model):
    image=models.ImageField(upload_to='restuarant/')
    title=models.CharField(max_length=255)
    description=RichTextUploadingField()
    breakfast=models.TimeField(blank=True,null=True)
    lunch=models.TimeField(blank=True,null=True)
    dinner=models.TimeField(blank=True,null=True)
    video=models.CharField(max_length=1000,default='https://www.youtube.com/watch?v=pq3Otf0zbdk&ab_channel=ShotByEnis')

    def __str__(self) -> str:
        return f'{self.title}'
    
    # def save(self,*args,**kwargs):
    #     if self.image:
    #         a=PhotoGallery.objects.create(image=self.image)
    #         b=VideoGallery.objects.create(video=self.video,image=self.image)


    #     return super().save(*args,**kwargs) 


class CategoryMenu(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.title}'   

class Menu(models.Model):
    category=models.ForeignKey(CategoryMenu,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.title}' 

