from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f'{self.first} {self.last}'

class Listings(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    bid = models.CharField(max_length = 100)
    category = models.CharField(max_length = 200)
    image = models.ImageField(default ='No Image', upload_to = 'images')

    def __str__(self):
        return f' The title is: {self.title} The content is: {self.description} The current bid is: {self.bid} The caption is: {self.category} The image is: {self.image}' 


class Bids():
    pass

class Comments():
    pass



# class CreateForm(forms.Form):
#   title = forms.CharField(label="Title")
#   content = forms.CharField(label = "Contents", widget=forms.Textarea)
#   bid_amount = forms.CharField(label="bid")

# class EditForm(forms.Form):
#     content = forms.CharField(label="Contents", widget=forms.Textarea)
#     bid_amount = forms.CharField(label="bid")

#     def set_values(self, title, content, bid_amount):
#       self.entry_bid_amount = bid_amount
#       self.entry_title = title
#       self.entry_content = content