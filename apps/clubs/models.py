from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from apps.home.models import PhotoGallery


class ClubsInfo(models.Model):
    title=models.CharField(max_length=255)
    description=RichTextUploadingField()
    
    def __str__(self) -> str:
        return f'{self.title}' 
    
class Clubs(models.Model):
    title=models.CharField(max_length=255)
    description=RichTextUploadingField()
    photo=models.ImageField(upload_to='clubs/')
    from_time=models.TimeField()
    to_time=models.TimeField()

    def __str__(self) -> str:
        return f'{self.title}' 

    # def save(self,*args,**kwargs):
    #     if self.photo:
    #         a=PhotoGallery.objects.create(image=self.photo)


        # return super().save(*args,**kwargs) 

class SpaEtiquette(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    
    def __str__(self):
        return self.title
