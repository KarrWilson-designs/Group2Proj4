// Function to open data repository
function openDataRepo() {
    alert("Opening data repository...");
    // Replace this alert with a link to your actual repository
}

// Perform search functionality
function performSearch() {
    const arrow = "fa fa-arrow-circle-o-right";
    const query = document.getElementById("search").value;
    if (query) {
        alert(`If you're searching for: ${query} ${arrow} scroll down/click the related button`);
        // You could implement actual search functionality here
    } else {
        alert("Please enter a search term.");
    }
}

// Smooth scrolling for navigation icons
document.querySelectorAll(".nav-icons a").forEach((link) => {
    link.addEventListener("click", function (event) {
        event.preventDefault();
        const targetSection = document.querySelector(this.getAttribute("href"));
        targetSection.scrollIntoView({ behavior: "smooth", block: "start" });
    });
});
