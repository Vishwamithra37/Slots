function submitForm(e) {
    e.preventDefault();
  
    const name = document.getElementById("name").value;
    const description = document.getElementById("description").value;
    const slot_duration = document.getElementById("slot_duration").value;
    const total_slots = document.getElementById("total_slots").value;
    const start_date = document.getElementById("start_date").value;
    const end_date = document.getElementById("end_date").value;
    const slot_open_time = document.getElementById("slot_open_time").value;
    const slot_close_time= document.getElementById("slot_close_time").value;
    const max_bookings_per_slot = document.getElementById("max_bookings_per_slot").value;
    const admin_id = document.getElementById("admin_id").value;

    
    fetch("/Create_resource", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name,
            description,
            slot_duration,
            total_slots,
            start_date,
            end_date,
            slot_open_time,
            slot_close_time,
            max_bookings_per_slot,
            admin_id 





          
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          // Redirect to the home page if login is successful
           window.location.href = "/about";
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
    
    document.getElementById("admin_resource_form").addEventListener("submit", submitForm);
    