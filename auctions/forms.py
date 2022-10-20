from django.forms import ModelForm
from django.forms import fields  
from . import models 
from django import forms

class CreateListing(ModelForm):
  class Meta:
    model = models.Listings
    fields = '__all__'
