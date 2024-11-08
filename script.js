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

//button function for data analysis visuals

function openDataRepo() {
    document.querySelectorAll(".data-vis-img").forEach((image) => {
        image.style.display = "block";
    });
}

// very unimportant but fun search button function. Source: ChatGPT
function performSearch() {
    const query = document.getElementById("search").value;
    const searchTerms = ["intro", "lit-review", "data", "discussion", "conclusion"];

    //if the search term is not included in the above list of terms
    if (!searchTerms.includes(query)) {
        alert("I meant it when I said this was for aesthetics... Please enter a search term tho.");
    }
    // if search query is included
    else {
        alert(
            `I meant it when I said this was for aesthetics... If you're searching for: ${query}, scroll down/click the related button`
        );
    }
}
