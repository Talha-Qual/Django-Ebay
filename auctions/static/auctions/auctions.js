document.addEventListener('DOMContentLoaded', function() {

document.querySelector("#watchlist-add-form").onsubmit = ()=> {
  form = document.querySelector('#watchlist-add-form');
  const formData = new FormData(form);
  fetch(form.action, {
    method: "GET",
    body: formData
  })
  .then(response => {
    return response.json()})
    .then(data => {
      console.log(data);
      document.querySelector('#no-bell').src="/media/images/bell_icon.png"
    })
    .catch(error => {
      console.log('**Error**', error);
    })
  }
  document.querySelector("#watchlist-remove-form").onsubmit = ()=> {
    form = document.querySelector('#watchlist-remove-form');
    const formData = new FormData(form);
    fetch(form.action, {
      method: "GET",
      body: formData
    })
    .then(response => {
      return response.json()})
      .then(data => {
        console.log(data);
        document.querySelector('#bell').src= "/media/images/crossed_out_bell.jpg"
      })
      .catch(error => {
        console.log('**Error**', error);
      })
    }
})