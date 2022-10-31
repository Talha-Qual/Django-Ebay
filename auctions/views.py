from os import access
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import CreateComment, CreateListing
from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse

from .models import User, Listings, Watchlist, Bids, Comments


def index(request):
    listings = Listings.objects.filter(active=1)
    return render(request, "auctions/index.html", {
        "listings": listings,
        "length": len(listings)
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

@login_required(login_url='login')
def create_listing(request):
    if request.method == "POST":
        form = CreateListing(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # bid = form.cleaned_data['bid']
            # Find a way to save the entry here
            return redirect('index')
        else:
            return render(request, "auctions/create_listing.html", {"form": form})
    return render(request, "auctions/create_listing.html", {"form": CreateListing()})

# if "watch" in request.POST:
#     try:
#         watchlist = Watchlist.objects.get(user_id=request.user.id)
#     except:
#         watchlist = Watchlist(user_id=request.user.id)
@login_required(login_url='login')
def view_listing(request, item):
    if request.method == "POST":
        # add a listing to your watchlist
        if "watch" in request.POST:
            try:
                watchlist = Watchlist.objects.get(user_id =request.user.id, listing_id = item)
                watchlist.active = True
                watchlist.save(update_fields=["active"])
                return redirect(reverse("view_listing", args = (item,)))
            except:
                watchlist = Watchlist(user_id = request.user.id, listing_id = item, active=True)
                watchlist.save()
                return redirect(reverse("view_listing", args = (item,)))
        if "unwatch" in request.POST:
            watchlist = Watchlist.objects.get(user_id = request.user.id, listing_id = item)
            watchlist.active = False
            watchlist.save(update_fields=["active"])
            return redirect(reverse("view_listing", args=(item,)))
        if "my_comment" in request.POST:
            comment_form = CreateComment(request.POST)
            if comment_form.is_valid():
                instance = comment_form.save(commit=False)
                instance.user = request.user
                instance.listing_id = item
                instance.timestamp = timezone.localtime()
                instance.save()
                return redirect(reverse("view_listing", args=(item,)))
            else:
                return render(request, "auctions/listing.html", {
                    "comment_form":comment_form
                })
        # BIDS not working properly :( 
        if "bid" in request.POST:
            listing = Listings.objects.get(pk = item)
            price = listing.price
            bid = int(request.POST.get("amount"))
            min = price
            # pretty sure that the following code is always causing highest to be set to 0
            try:
                highest = Bids(user_id = request.user.id, listing_id = item).last()
            except:
                highest = 0

            if bid < price and bid <= highest:
                # pretty sure this code is noever going to get run
                return render(request, "auctions/view_listing.html")
                # add error message here
            else:
                bids = Bids(user_id=request.user.id, listing_id = item, bid = bid)
                bids.save()
                highestbid = Listings.objects.get(pk=item)
                highestbid.highestbid = bid
                highestbid.save(update_fields=["highestbid"])
                return redirect(reverse("view_listing", args=(item,)))
        if "close" in request.POST:
            listing = Listings.objects.get(pk = item)
            listing.active = False
            # pretty sure that django is smart enough to know which fields on an object have changed
            listing.save(update_fields=["active"])
            return redirect(reverse("index"))
    else:
        f = get_object_or_404(Listings, pk = item)
        # try:
        #     f = Listings.objects.get(pk = item)
        # except Listings.DoesNotExist:
        #     raise Http404("Listing not found")

        try:
            watching = Watchlist.objects.get(user_id = request.user.id, listing_id = item)
        except:
            watching = None


        # filter will return an empty list. without looking as listing.html, 
        # i don't see why bids=0 is better than bigs=[]. but just looking at 
        # listing.html, you don't use bids
        # try:
        #     bids = Bids.objects.filter(listing_id = item)
        # except:
        #     bids = 0
        bids = Bids.objects.filter(listing_id = item)

        # you don't need listing=..., and if you did, you have it already in variable f.
        # The call to filter().last() won't raise an exception
        # try:
        #     listing = Listings.objects.get(pk=item)
        #     winner = Bids.objects.filter(listing_id = item).last()
        # except:
        #     winner = None

        winner = Bids.objects.filter(listing_id = item).last()
        return render(request, "auctions/listing.html", {
            "bid": bids,
            "total_bids": len(bids),
            "winner": winner,
            "listing": f,
            "watching": watching,
            "comments": Comments.objects.filter(listing_id=item),
            "categories": Listings.CATEGORY_CHOICES,
            "comment_form": CreateComment()
            })

@login_required(login_url='login')
# makes no sense torequire login, if there's is no code that relates to the logged in user!
def personal_listings(request):
    winners = []
    listings = Listings.objects.filter(active=0)
    for listing in listings:
        winner = Bids.objects.filter(listing_id=listing.id).last()
        winners.append(winner)
    zipped = zip(listings, winners)
    return render(request, "auctions/personal_listings.html", {
        "listings": listings,
        "length": len(listings),
        "winners": winners,
        "zipped": zipped,
        "listings": Listings.objects.filter(user=request.user)
    })

#@login_required(login_url='login')
def categories_view(request):
    return render(request, "auctions/categories.html", {
        "categories": Listings.CATEGORY_CHOICES
        })
    # try:
    #     category = Listings.objects.filter(category = category, active=True)
    # except:
    #     category = None
    # return render(request, "auctions/categories.html", {
    #     "listings": Listings.objects.all(),
    #     "category": category,
    #     "categories": Listings.CATEGORY_CHOICES
    #     })

@login_required(login_url='login')
def bids_page(request):
    return render(request, "auctions/bid.html", {
        "bids": Bids.objects.filter(user_id = request.user.id),
    })

def category_listing(request, category_id):
    listings = Listings.objects.filter(category = category_id)
    return render(request, "auctions/category_listing.html", {
            "listings": listings})
# @login_required(login_url='login')
# def category_listing(request, selection):
#     try:
#         category = Listings.objects.filter(category = selection)
#     except:
#         category = None
#     return render(request, "auctions/category_listing.html", {"category": category, "selection": selection, "categories": Listings.CATEGORY_CHOICES})

@login_required(login_url='login')
def watchlist_page(request):
    try:
        watchlist = Watchlist.objects.filter(user_id = request.user.id, active = True).values_list("listing_id")
        watching = Listings.objects.filter(id__in = watchlist)
    except:
        watching = 0
    return render(request, "auctions/watchlist.html", {"watching": watching, "watchlist": len(Watchlist.objects.filter(user_id=request.user.id)), "categories": Listings.CATEGORY_CHOICES})
