from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class NewsCategory(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'
    
class News(models.Model):

    category=models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    time=models.DateTimeField(auto_now_add=True ,blank=True,null=True)
    description=RichTextUploadingField()
    image = models.ImageField(upload_to=" media/")

    def __str__(self):
        return f'{self.title}'
    

class Comments(models.Model):

    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    text = models.TextField("Сообщение", max_length=5000)
    time_pub = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News,  on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True,related_name='children')

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering=['-pk']