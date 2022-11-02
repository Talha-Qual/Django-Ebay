document.addEventListener('load', function() {

document.querySelector('#watchlist-toggle').onsubmit = ()=> {
  form = document.querySelector('#toggle-watchlist');
  const formData = new FormData(form);
  fetch(form.action, {
    method: "POST",
    body: formData
  })
  .then(response => {
    return response.json()})
    .then(data => {
      if (data["current_status"] === "on") {
        document.querySelector('#bell').src = "/media/images/crossed_out_bell.jpg"
      }
      else {
        document.querySelector('#no-bell').src = "/media/images/bell_icon.png"
      }
    })
    .catch(error => {
      console.log('**Error**', error);
    })
    return false;
  }
})