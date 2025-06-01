

function verifyUser() {
  const username = document.getElementById("usernameInput").value.trim();
  const password = document.getElementById("passwordInput").value.trim();
  checkUserCreds(username, password);
}

function checkUserCreds(username, password) {
  const systemUsername = "Bond";
  const systemPassword = "007";
  const messageElem = document.getElementById("message");

  messageElem.style.display = "block";

 
  messageElem.classList.remove("success");
  messageElem.classList.remove("error");

  if (!username || !password) {
    messageElem.textContent = "Please enter both username and password.";
    messageElem.classList.remove("success");
    messageElem.classList.add("error");
    setTimeout(() => { messageElem.textContent = ""; }, 2000);
    return;
  }

  if (username === systemUsername && password === systemPassword) {
    messageElem.textContent = "Correct. Logging you in…";
    messageElem.classList.add("success");
    setTimeout(() => {
      messageElem.textContent = "";
    window.location.href = "dashboard.html";
    }, 2000);
  } 
  else {
    messageElem.textContent = "Username or password are incorrect";
    messageElem.classList.remove("success");
    messageElem.classList.add("error");
    setTimeout(() => { messageElem.textContent = ""; }, 2000);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const inputs = document.querySelectorAll("#usernameInput, #passwordInput");
  inputs.forEach(input => {
    input.addEventListener("keyup", function (e) {
      if (e.key === "Enter") {
        verifyUser();
      }
    });
  });
});