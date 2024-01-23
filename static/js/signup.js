
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function submitForm(e) {
  e.preventDefault();

  alert("iam here")

  const Fullname = document.getElementById("Fullname").value;
  const Email = document.getElementById("Email").value;
  const Contact_no = document.getElementById("Contact_no").value;
  const Password = document.getElementById("Password").value;
  const Confirm_password = document.getElementById("Confirm_password").value;

  // Validate email format
  if (!isValidEmail(Email)) {
    console.error("Invalid email format");
    // Handle invalid email (e.g., show an error message)
    return;
  }

  // Validate password (e.g., minimum length)
  // if (!isValidPassword(Password)) {
  //   console.error("Invalid password");
  //   // Handle invalid password (e.g., show an error message)
  //   return;
  // }
  

  fetch("/user_register", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      Fullname,
      Email,
      Contact_no,
      Password,
      Confirm_password
    }),
  })
  .then((response) => response.json())
  .then((data) => {
      // Redirect to the home page if login is successful
      window.location.href = "/login.html";
    })
  .catch((error) => {
    console.error("Error:", error);
  });
}


//document.getElementById("signup_form").addEventListener("submit", submitForm);
 document.getElementById("signup_form").addEventListener("submit", submitForm);

