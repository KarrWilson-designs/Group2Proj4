function showDiv(divId) {
    // Hide all title card images
    let titleCards = document.querySelectorAll(".titleCards .mainBits");
    titleCards.forEach((card) => {
        card.style.display = "none";
    });

    // Hide all divs with the class "hidden"
    let divs = document.querySelectorAll(".hidden");
    divs.forEach((div) => {
        div.style.display = "none";
    });

    // Show the div with the matching ID
    let targetDiv = document.getElementById(divId);
    if (targetDiv) {
        targetDiv.style.display = "block";
    }
}

function showTitleCards() {
    // Show all title card images
    let titleCards = document.querySelectorAll(".titleCards .mainBits");
    titleCards.forEach((card) => {
        card.style.display = "block";
    });

    // Hide all divs with the class "hidden"
    let divs = document.querySelectorAll(".hidden");
    divs.forEach((div) => {
        div.style.display = "none";
    });
}

function openDataRepo() {
    document.querySelectorAll(".data-vis-img").forEach((image) => {
        image.style.display = "block";
    });
}
