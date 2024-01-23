function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function isAlphabeticFullName(fullname) {
  const alphabeticRegex = /^[A-Za-z\s]+$/;
  return alphabeticRegex.test(fullname);
}

function isNumericContactNumber(contactNumber) {
  const numericRegex = /^\d+$/;
  return numericRegex.test(contactNumber) && contactNumber.length === 10;
}

function isStrongPassword(password) {
  // Requires at least one uppercase letter, one special character, one number, and a minimum length of 8 characters
  const strongPasswordRegex = /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9])(?=.*[a-z]).{8,}$/;
  return strongPasswordRegex.test(password);
}

function passwordsMatch(password, confirmPassword) {
  return password === confirmPassword;
}
function togglePasswordVisibility(passwordFieldId) {
  const passwordField = document.getElementById(passwordFieldId);
  const eyeIcon = document.getElementById('eyeIcon');

  if (passwordField.type === 'password') {
    passwordField.type = 'text';
    eyeIcon.textContent = '👁️‍🗨️';
  } else {
    passwordField.type = 'password';
    eyeIcon.textContent = '👁️';
  }
}

function submitForm(e) {
  e.preventDefault();

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

  // Validate full name
  if (!isAlphabeticFullName(Fullname)) {
    console.error("Full name must contain only letters");
    // Handle invalid full name (e.g., show an error message)
    return;
  }

  // Validate contact number
  if (!isNumericContactNumber(Contact_no)) {
    console.error("Contact number must contain only numbers and be 10 characters long");
    // Handle invalid contact number (e.g., show an error message)
    return;
  }

  // Validate strong password
  if (!isStrongPassword(Password)) {
    console.error("Password must contain at least one uppercase letter, one special character, one number, and be 8 characters long");
    // Handle invalid password (e.g., show an error message)
    return;
  }

  // Check if password and confirm password match
  if (!passwordsMatch(Password, Confirm_password)) {
    console.error("Password and confirm password do not match");
    // Handle password mismatch (e.g., show an error message)
    return;
  }

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
      Confirm_password,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      // Redirect to the home page if login is successful
       window.location.href = "/loginpage";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

document.getElementById("signup_form").addEventListener("submit", submitForm);
