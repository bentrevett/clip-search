document
    .getElementById("searchInput")
    .addEventListener("keyup", function (event) {
        // Check if the key pressed is 'Enter'
        if (event.key === "Enter") {
            // Prevent the default action to avoid submitting the form if it's part of one
            event.preventDefault();
            // Trigger the click event on the Search button
            document.getElementById("search").click();
        }
    });

document.getElementById("search").addEventListener("click", async function () {
    const searchResults = document.getElementById("searchResults");
    searchResults.innerHTML = "Loading...";
    const searchText = document.getElementById("searchInput").value;
    const data = await lookup(searchText);
    console.log("Received data:", data);
    searchResults.innerHTML = "";
    data.imagePaths.forEach((imagePath, index) => {
        const similarityScore = data.similarity[index];
        const imageHeaderElement = createImageHeaderElement(
            imagePath,
            similarityScore
        );
        searchResults.appendChild(imageHeaderElement);
        const imgElement = createImageElement(imagePath);
        searchResults.appendChild(imgElement);
    });
});
async function lookup(searchText) {
    const url = "http://localhost:4000/lookup";
    const data = { text: searchText };

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        const jsonData = await response.json();
        return jsonData;
    } catch (error) {
        console.error("Error fetching data:", error);
        return null;
    }
}
function createImageHeaderElement(imagePath, similarityScore) {
    const imageNameElement = document.createElement("p");
    imageNameElement.innerText = `Path: ${imagePath}\nSimilarity: ${similarityScore.toFixed(
        2
    )}`;
    return imageNameElement;
}
function createImageElement(imagePath) {
    const imgElement = document.createElement("img");
    imgElement.src = imagePath;
    imgElement.style.width = "300px";
    imgElement.style.height = "300px";
    imgElement.alt = imagePath;
    return imgElement;
}
