document.addEventListener('DOMContentLoaded', function() {
  update_watchlist();
});

function update_watchlist() {
  // not sure how the fetch will work when we have to pass in the item as an arg for view_listing
  fetch("/view_listing/3")
  .then(response => response.json())
  .then(data => {
    if (data['watchlist_status'] == true) {
      document.querySelector('#bell').src="/media/images/crossed_out_bell.jpg"
    }
    else {
      document.querySelector('#bell').src="/media/images/bell_icon.png"
    }
  })

  .catch(error => {
    console.log('**Error**', error);
  });
  
;}