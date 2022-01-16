from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from time import time
import random


def gen_slug(k):
    new_slug = slugify(k, allow_unicode=True)
    return f'{new_slug}-{str(int(time()))}'


class Employee(AbstractUser):
    full_name = models.CharField(max_length=40, default=None)
    slug = models.SlugField(max_length=150, blank=True, unique=True, default=None)
    position = models.ForeignKey('Position', on_delete=models.RESTRICT, blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.RESTRICT, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.username)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('employee_detail_url', kwargs={'slug': self.slug})



class Position(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('position_detail_url', kwargs={'slug': self.slug})


    def get_update_url(self):
        return reverse('position_update_url', kwargs={'slug': self.slug})


    def get_delete_url(self):
        return reverse('position_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return f'{self.title}'


class Department(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('department_detail_url', kwargs={'slug': self.slug})


    def get_update_url(self):
        return reverse('department_update_url', kwargs={'slug': self.slug})


    def get_delete_url(self):
        return reverse('department_delete_url', kwargs={'slug': self.slug})


    def __str__(self):
        return f'{self.title}'


