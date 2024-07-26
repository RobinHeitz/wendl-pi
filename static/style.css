
document.addEventListener("DOMContentLoaded", function() {
    const checkbox = document.getElementById("myCheckbox");
    checkbox.addEventListener("change", function() {
        const checked = checkbox.checked;
        fetch("/checkbox", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ checked: checked })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Server response:", data);
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
