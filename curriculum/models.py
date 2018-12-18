from django.db import models
from ckeditor.fields import RichTextField


class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return self.company


class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return self.school


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
