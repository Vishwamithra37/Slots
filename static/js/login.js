function isStrongPassword(password) {
  // Password should be at least 6 characters long
  const strongPasswordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9])(?=.*[a-z]).{8,}$/;
  return strongPasswordRegex.test(password);
}
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}


function submitForm(e) {
  e.preventDefault();

  const Email = document.getElementById("Email").value;
  const Password = document.getElementById("Password").value;

  // Validate email format
  if (!isValidEmail(Email)) {
    console.error("Invalid email format");
    // Handle invalid email (e.g., show an error message)
    return;
  }

  // Validate password (e.g., alphanumeric with minimum length)
  if (!isStrongPassword(Password)) {
    console.error('Invalid password');
    // Handle invalid password (e.g., show an error message)
    return;
  }

  fetch("/user_login", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ Email, Password }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Redirect to the home page if login is successful
      window.location.href = "/home";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

document.getElementById("login_form").addEventListener("submit", submitForm);
