import uuid
import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

def generate_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex}.{ext}'
    return os.path.join('projects/', filename)


class PostProjects(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=generate_unique_filename)
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(800, 600)],
                                    format='JPEG',
                                    options={'quality': 80})
    description = models.TextField()

    def __str__(self):
        return self.title