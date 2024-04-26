document.getElementById("search").addEventListener("click", async function () {
    const searchResults = document.getElementById("searchResults");
    searchResults.innerHTML = "Loading...";
    const data = await lookup();
    console.log("Received data:", data);
    const imageNames = [
        "red-hat-1.jpg",
        "red-shirt-1.jpg",
        "blue-hat-1.jpg",
        "blue-shirt-1.jpg",
    ];
    searchResults.innerHTML = "";
    imageNames.forEach((imageName) => {
        const imageNameElement = createImageNameElement(imageName);
        searchResults.appendChild(imageNameElement);
        const imgElement = createImageElement(imageName);
        searchResults.appendChild(imgElement);
    });
});
async function lookup() {
    const url = "http://localhost:4000/lookup";
    const data = { text: "a red shirt" };

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
function createImageNameElement(imageName) {
    const imageNameElement = document.createElement("p");
    imageNameElement.innerText = imageName;
    return imageNameElement;
}
function createImageElement(imageName) {
    const imgElement = document.createElement("img");
    imgElement.src = `images/${imageName}`;
    imgElement.style.width = "300px";
    imgElement.style.height = "300px";
    imgElement.alt = imageName;
    return imgElement;
}
