
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
      console.log(`xximageid ${image_id}`);
      const formData = new FormData(form);
      fetch(form.action, {
        method: "POST",
        body: formData
      })
      .then(response => {
        return response.json()})
      .then(data => {
        if (data["current_status"] === "off") {
          document.querySelector(image_id).src = "/media/images/crossed_bell.png"
        }
        else if (data["current_status"] === "on") {
          document.querySelector(image_id).src = "/media/images/bell_icon.png"
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
})