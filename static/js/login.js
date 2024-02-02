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
  const emailInput = document.getElementById("Email");
  const passwordInput = document.getElementById("Password");

  const emailError = document.getElementById("email-error");
  const passwordError = document.getElementById("password-error");

  const Email = emailInput.value.trim();
  const Password = passwordInput.value.trim();
  // Validate email format
  if (!isValidEmail(Email)) {
    console.error("Invalid email format");
    // Display error message for email
    emailError.textContent = "Invalid email format";
    // Clear any existing error messages for password and login
    passwordError.textContent = "";
    loginError.textContent = "";
    return;
}

// Validate password (e.g., alphanumeric with minimum length)
if (!isStrongPassword(Password)) {
    console.error('Invalid password');
    // Display error message for password
    passwordError.textContent = "Invalid password";
    // Clear any existing error messages for email and login
    emailError.textContent = "";
  
    return;
}

// Clear any existing error messages
emailError.textContent = "";
passwordError.textContent = "";


// Continue with form submission or other actions
// ...


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
