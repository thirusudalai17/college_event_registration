function validateForm() {
    const name = document.getElementById("name").value.trim();
    const registerNo = document.getElementById("register_no").value.trim();
    const department = document.getElementById("department").value;
    const year = document.getElementById("year").value;
    const event = document.getElementById("event").value;
    const email = document.getElementById("email").value.trim();
    const error = document.getElementById("error-message");

    if (!name || !registerNo || !department || !year || !event || !email) {
        error.textContent = "Please fill all fields.";
        return false;
    }

    if (name.length < 3) {
        error.textContent = "Name must contain at least 3 characters.";
        return false;
    }

    error.textContent = "";
    return true;
}
