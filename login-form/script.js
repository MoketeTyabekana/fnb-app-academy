
// This script handles the login form submission and user verification.

function verifyUser(){
let username = document.getElementById("usernameInput").value;
let password = document.getElementById("passwordInput").value;
checkUserCreds(username, password);
}
// This function checks the user credentials against a predefined list of users.
// For simplicity, this example uses a hardcoded list of users.
function checkUserCreds(username,password){

  let systemUsername = "Bond";
let systemPassword = "007";

if (username === systemUsername && password === systemPassword) {
    document.getElementById("message").innerHTML = "Correct. Logging you in…";
} else {
    document.getElementById("message").innerHTML = "Username or password are incorrect";
}

}