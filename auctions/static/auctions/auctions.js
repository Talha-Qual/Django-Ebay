document.addEventListener('DOMContentLoaded', function() {

document.querySelector("#watchlist-status-form").onsubmit = ()=> {
  form = document.querySelector('#watchlist-status-form');
  const formData = new FormData(form);
  fetch(form.action, {
    method: "POST",
    body: formData
  })
  .then(response => {
    return response.json()})
    .then(data => {
      console.log(data);
      if (data['current_status'] == "on") {
        document.querySelector('#no-bell').src="/media/images/bell_icon.png"
      }
      else if (data['current_status'] == "off") {
        document.querySelector('#bell').src="/media/images/crossed_out_bell.jpg"
      }
    })
    .catch(error => {
      console.log('**Error**', error);
    })
    return false;
  }
})

// function update_watchlist() {
//   // not sure how the fetch will work when we have to pass in the item as an arg for view_listing
//   fetch("/view_listing/3")
//   .then(response => response.json())
//   .then(data => {
//     if (data['watchlist_status'] == "on") {
//       document.querySelector('#no-bell').src="/media/images/crossed_out_bell.jpg"
//     }
//     else {
//       document.querySelector('#no-bell').src="/media/images/bell_icon.png"
//     }
//   })

//   .catch(error => {
//     console.log('**Error**', error);
//   });
  
// ;}
// }
// });