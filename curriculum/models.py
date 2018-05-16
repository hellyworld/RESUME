from django.db import models
from ckeditor.fields import RichTextField


class Experience(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField()


class Education(models.Model):
    school = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField()


class Category(models.Model):
    name = models.CharField(max_length=50)


class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=50)
