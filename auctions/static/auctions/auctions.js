document.addEventListener('DOMContentLoaded', function() {
watchlist_toggle_get();
})
function watchlist_toggle_post() {
  document.querySelector('#watchlist-toggle').onsubmit = ()=> {
  form = document.querySelector('#watchlist-toggle');
  const formData = new FormData(form);
  fetch(form.action, {
    method: "POST",
    body: formData
  })
  .then(response => {
    return response.json()})
    .then(data => {
      if (data["icon_status"] === "off") {
        document.querySelector('#bell').src = "/media/images/crossed_bell.png"
      }
      else if (data["icon_status"] === "on") {
        document.querySelector('#bell').src = "/media/images/bell_icon.png"
      }
      else {
        console.log("We ran into an error :( ")
      }
    })
    .catch(error => {
      console.log('**Error**', error);
    })
    return false;
  }
}

function watchlist_toggle_get() {
  document.querySelector('#watchlist-toggle').onsubmit = ()=> {
    fetch(`/api/watchlist_toggle/${listing_id}`).then(response => {
      return response.json().then(data => {
        if (data["icon_status"] === "off") {
          document.querySelector('#bell').src = "/media/images/crossed_bell.png"
        }
        else if (data["icon_status"] === "on") {
          document.querySelector('#bell').src = "/media/images/bell_icon.png"
        }
        else {
          console.log("We ran into an error :( ")
        }
      })
      .catch(error => {
        console.log('**Error**', error);
      })
    })
  }
}


