from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class hakkimda(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    etiket = models.CharField(max_length=200, blank=True, null=True)
    onhome = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"

class post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True,upload_to="images/")
    etiket = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=250)
    content = RichTextField(blank=True, null=True)
    onhome = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"
