document.addEventListener('DOMContentLoaded', function() {
  update_watchlist();
  setInterval(update_watchlist, 1000)
});

function update_watchlist() {
  // not sure how the fetch will work when we have to pass in the item as an arg for view_listing
  fetch("/view_listing")
}