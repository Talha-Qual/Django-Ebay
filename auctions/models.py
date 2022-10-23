from io import open_code
from unittest.util import _MAX_LENGTH
from xmlrpc.client import TRANSPORT_ERROR
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    bid = models.CharField(max_length = 100)
    image = models.ImageField(default ='No Image', upload_to = 'images')
    user = models.ForeignKey(User, blank = True, null = True, on_delete=models.CASCADE)

    TECH = 'TCH'
    CLOTHING = 'CLT'
    UNKNOWN = 'UNK'
    FOOD = 'FOD'
    ART = 'ART'
    ACCESSORIES = 'AC'


    CATEGORY_CHOICES = [
    (TECH, 'Technology'),
    (FOOD, 'Food'),
    (ART, 'Art'),
    (CLOTHING, 'Clothing'),
    (UNKNOWN, 'Unknown'),
    (ACCESSORIES, 'Accessories'),
    ]

    category = models.CharField(max_length = 3, choices = CATEGORY_CHOICES, blank = True)

    def __str__(self):
        return f' The title is: {self.title} The content is: {self.description} The current bid is: {self.bid} The caption is: {self.category} The image is: {self.image}' 


class Bids():
    offer = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} placed a bid for ${self.offer} for {self.listing.title}'

class Comments():
    comment = models.TextField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} wrote '{self.comment}'' on {self.listing.title}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)


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