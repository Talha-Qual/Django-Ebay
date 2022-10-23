from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import CreateListing
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse

from .models import User, Listings



def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all(),
        "categories": Listings.CATEGORY_CHOICES,
    }
    )

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url='register')
def create_listing(request):
    if request.method == "POST":
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # bid = form.cleaned_data['bid']
            # Find a way to save the entry here
            form.save()
            return redirect('index')
        else:
            return render(request, "auctions/create_listing.html", {"form": form})
    return render(request, "auctions/create_listing.html", {"form": CreateListing()})

@login_required(login_url='register')
def view_listing(request, title):
    try:
        f = Listings.objects.get(title = title)
    except Listings.DoesNotExist:
        raise Http404("Listing not found")
    return render(request, "auctions/listing.html", {"listing": f})

@login_required(login_url='register')
def categories_view(request):
    try:
        category = Listings.objects.filter(category=selection, active=True)
    except:
        category = None
    return render(request, "auctions/categories.html", {
        "listings": Listings.objects.all(),
        "category": category,
        "total_items": len(Listings.objects.filter(user_id=request.user.id)),
        "categories": Listings.CATEGORY_CHOICES
        })