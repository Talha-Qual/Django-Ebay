from django.forms import ModelForm
from django.forms import fields  
from . models import *
from django import forms

class CreateListing(ModelForm):
  class Meta:
    model = Listings
    fields = ['title', 'price', 'description', 'image', 'category']

class CreateComment(ModelForm):
  class Meta:
    model = Comments
    fields = ['comment']