from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.URLField(max_length=700, null=True, blank=True)
    twitter = models.URLField(max_length=700, null=True, blank=True)
    instagram = models.URLField(max_length=700, null=True, blank=True)
    linkedin = models.URLField(max_length=700, null=True, blank=True)
    whatsapp = models.URLField(max_length=700, null=True, blank=True)
    avatar = models.ImageField(null=True)

    title_head = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)

    contact_body = models.TextField(null=True)

    def __str__(self):
        return str(self.name)

class Work(models.Model):
    title = models.CharField(max_length=100, null=True)
    desc = RichTextField(null=True)
    image = models.ImageField(null=True)
    link = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

class Skill(models.Model):
    skill_name = models.CharField(max_length=100, null=True)
    desc = RichTextField(null=True)
    image =  models.ImageField(null=True)
    image_hover =  models.ImageField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.skill_name)

class Portfolio(models.Model):
    title = models.CharField(max_length=100, null=True)
    link = models.URLField(max_length=700, null=True, blank=True)
    desc = RichTextField(null=True)
    image = models.ImageField(upload_to='portfolio/', null=True)
    web = models.BooleanField(default=False)
    mobile = models.BooleanField(default=False)
    others = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

class Contact(models.Model):
    name = models.CharField(max_length=700, null=True)
    email = models.EmailField(max_length=700, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)
