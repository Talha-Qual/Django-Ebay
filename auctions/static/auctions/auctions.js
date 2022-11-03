document.addEventListener('DOMContentLoaded', function() {

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
      if (data["current_status"] === "off") {
        document.querySelector('#bell').src = "/media/images/crossed_bell.png"
      }
      else if (data["current_status"] === "on") {
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
})