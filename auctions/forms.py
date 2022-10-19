from django.forms import ModelForm
from . import models

class CreateListing(ModelForm):
  class Meta:
    model = models.Listings
    fields = ['title', 'content', 'bid']