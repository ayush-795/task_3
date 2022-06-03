from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
category_choice = (
		('Furniture', 'Furniture'),
		('IT Equipment', 'IT Equipment'),
		('Phone', 'Phone'),
        ('Electronic','Electronic')
	)

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name

class Stock(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    item_name=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(default='0',blank=True,null=True)
    issue_quantity=models.IntegerField(default='0',blank=True,null=True)
    issue_by=models.CharField(max_length=50,blank=True,null=True)
    issue_to=models.CharField(max_length=50,blank=True,null=True)
    last_updated=models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)


class StockHistory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    item_name=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(default='0',blank=True,null=True)
    issue_quantity=models.IntegerField(default='0',blank=True,null=True)
    issue_by=models.CharField(max_length=50,blank=True,null=True)
    issue_to=models.CharField(max_length=50,blank=True,null=True)
    last_updated=models.DateTimeField(auto_now_add=False, auto_now=False)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)