const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    if (username === "" || password === "") {
        message.style.color = "red";
        message.textContent = "Please enter username and password";
    } else if (username === "admin" && password === "admin123") {
        message.style.color = "green";
        message.textContent = "Login Successful!";
    } else {
        message.style.color = "red";
        message.textContent = "Invalid Username or Password";
    }
});
