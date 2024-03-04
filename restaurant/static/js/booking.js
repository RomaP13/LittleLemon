const dataset = document.currentScript.dataset;
const bookingsUrl = dataset.bookingsUrl;

const date = new Date()
document.getElementById("id_reservation_date").value = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`

getBookings()

document.getElementById("id_reservation_date").addEventListener("change", function () {
  getBookings()
})


function getBookings() {
  let reserved_slots = []
  const date = document.getElementById("id_reservation_date").value
  document.getElementById("today").innerHTML = date
  
  fetch(bookingsUrl + "?date=" + date)
    .then(r => r.json())
    .then(data => {
      reserved_slots = []
      bookings = ""
      for (item of data) {
        reserved_slots.push(item.reservation_time)
        bookings += `<p>${item.first_name} - ${formatTime(item.reservation_time)}</p>`
      }

      slot_options = "<option value="0" disabled>Select time</option>"
      for (i = 10; i <= 20; i++) {
        const label = formatTime(i)
        if (reserved_slots.includes(i)) {
          slot_options += `<option value=${i} disabled>${label}</option>`
        } else {
          slot_options += `<option value=${i}>${label}</option>`
        }

      }
      
      document.getElementById("id_reservation_time").innerHTML = slot_options
      if(bookings==""){
        bookings = "No bookings"
      }
      document.getElementById("bookings").innerHTML = bookings
    })
}

function formatTime(time) {
  const ampm = time < 12 ? "AM" : "PM"
  const t = time < 12 ? time : time > 12 ? time - 12 : time
  const label = `${t} ${ampm}`
  return label
}


document.getElementById("submit").addEventListener("submit", function () {
  const formdata = {
    first_name: document.getElementById("id_first_name").value,
    last_name: document.getElementById("id_last_name").value,
    email: document.getElementById("id_email").value,
    phone_number: document.getElementById("id_phone_number").value,
    reservation_date: document.getElementById("id_reservation_date").value,
    reservation_time: document.getElementById("id_reservation_time").value,
  }

  fetch(bookingsUrl, { method: "post", body: JSON.stringify(formdata) })
    .then(r => r.text())
    .then(data => {
      getBookings()
    })
})
