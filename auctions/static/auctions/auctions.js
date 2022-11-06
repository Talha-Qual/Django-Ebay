
            document.addEventListener('DOMContentLoaded', ()=> {
              document.querySelectorAll('.color-changer').forEach(button => {
                  button.onclick = function() {
                      document.querySelector('#hello').style.color = button.dataset.clr;
                  }
              }) 
          })


document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.watchlist-toggle').forEach(form => {
    form.onsubmit = function() {
      const image_id = "#bell"+form.dataset.listing_id;
      const formData = new FormData(form);
      fetch(form.action, {
        method: "POST",
        body: formData
      })
      .then(response => {
        return response.json()})
      .then(data => {
        if (data["current_status"]) {
          document.querySelector(image_id).src = "/media/images/bell_icon.png"
        }
        else {
          document.querySelector(image_id).src = "/media/images/crossed_bell.png"
        }
      })
      .catch(error => {
        console.log('**Error**', error);
      })
      return false;
    }
  })
})