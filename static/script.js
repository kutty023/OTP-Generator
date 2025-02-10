let selectedMethod = "";

// Function to select OTP method
function selectOTP(method) {
    selectedMethod = method;
    
    // Remove previous selection highlight
    document.querySelectorAll(".otp-button").forEach(btn => btn.classList.remove("selected"));

    // Highlight the selected button
    document.getElementById(method).classList.add("selected");

    // Clear the previous OTP when a new method is selected
    document.getElementById("otp-display").innerText = "----";
}

// Function to generate OTP
function generateOTP() {
    if (!selectedMethod) {
        alert("Please select an OTP method!");
        return;
    }

    fetch("/generate_otp", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ method: selectedMethod })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("otp-display").innerText = data.otp || "Error!";
    })
    .catch(err => {
        console.error("Error: ", err);
    });
}
