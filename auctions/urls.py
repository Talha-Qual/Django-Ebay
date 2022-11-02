from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("personal_listings", views.personal_listings, name="personal_listings"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("view_listing/<int:item>", views.view_listing, name="view_listing"),
    path("categories_view", views.categories_view, name="categories_view"),
    path("category_listing/<str:selection>", views.category_listing, name="category_listing"),
    path("watchlist_page", views.watchlist_page, name="watchlist_page"),
    path("my_bids", views.bids_page, name="bids"),
    # path("api/watchlist_add/<int:item>", views.api_watchlist_add, name = 'watchlist_add'),
    # path("api/watchlist_remove/<int:item>", views.api_watchlist_remove, name = 'watchlist_remove')
    path("api/watchlist_toggle/<int:item>", views.api_watchlist_toggle, name = 'watchlist_toggle')

]
