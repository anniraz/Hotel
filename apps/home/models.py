from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class SocialAccaunts(models.Model):
    title=models.CharField(max_length=100)
    icon=models.ImageField(upload_to='icons/')
    link=models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.title}'


class PhotoGallery(models.Model):
    image=models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f'image №{self.id}'

class VideoGallery(models.Model):
    video=models.CharField(max_length=500)
    image=models.ImageField(upload_to='gallery/',null=True, blank=True)

    def __str__(self):
        return f'video №{self.id}'


class AboutHotel(models.Model):

    title=models.CharField(max_length=255)
    description=RichTextUploadingField()
    photo=models.ImageField(upload_to='hotel/',null=True,blank=True)
    video=models.CharField(max_length=1000)
    address=models.CharField(max_length=500)
    map_address=models.CharField(max_length=500)
    phone = models.IntegerField(null=True, blank=True)
    email=models.EmailField(default='zarinakudajberdikyzy@gmail.com')
    accounts=models.ManyToManyField(SocialAccaunts)

    def __str__(self):
        return f'{self.title}'
    
    # def save(self,*args,**kwargs):
    #     if self.photo:
    #         a=PhotoGallery.objects.create(image=self.photo)
    #     return super().save(*args,**kwargs) 
        

class HotelFacilities(models.Model):
    # удобства отеля 
    icon=models.ImageField(upload_to='icons/')
    title=models.CharField(max_length=255)
    description=RichTextUploadingField()

    def __str__(self):
        return f'{self.title}'    

class TeamsSocialAccaunts(models.Model):

    title=models.CharField(max_length=100)
    icon=models.ImageField(upload_to='icons/')
    link=models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.title}'

class OurTeam(models.Model):
    image=models.ImageField(upload_to='our_team/')
    full_name=models.CharField(max_length=100)
    job=models.CharField(max_length=255)
    email=models.EmailField()
    accounts=models.ManyToManyField(TeamsSocialAccaunts)

    def __str__(self):
        return f'{self.full_name}'
    
    # def save(self,*args,**kwargs):
    #     if self.image:
    #         a=PhotoGallery.objects.create(image=self.image)


    #     return super().save(*args,**kwargs)  


class ExtraServicesInfo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

class ExtraServicesPoints(models.Model):
    points=models.CharField(max_length=100)

    def __str__(self):
        return self.points



class ExtraServices(models.Model):

    PRICE_PER=(
        ('month','month'),
        ('daily','daily'),
    )
    title=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    photo=models.ImageField(upload_to='hotel/',null=True,blank=True)
    price_per=models.CharField(max_length=50,choices=PRICE_PER) 
    points=models.ManyToManyField(ExtraServicesPoints)

    def __str__(self):
        return self.title




class ContactUs(models.Model):
    
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    subject=models.CharField(max_length=255)
    message=models.TextField()

    def __str__(self):
        return self.name



class Reviews(models.Model):

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    
    full_name=models.CharField(max_length=255)
    email=models.EmailField()
    text = models.TextField("Сообщение", max_length=5000)
    rating = models.IntegerField(choices=RATING ,blank=True, null=True)
    time_pub = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return f"{self.full_name} {self.rating}"
