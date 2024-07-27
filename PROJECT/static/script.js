function filter() {
    divs = document.getElementsByTagName("tr");
    veg = document.getElementById("vegan").checked
    alc = document.getElementById("alcohol").checked

    for (let x = 1; x < divs.length; x++) {
        const div = divs[x];
        const content = div.textContent.trim();

        div.style.display = 'table-row';
        if (content.indexOf("Ve") == -1 && veg) {
            div.style.display = 'none';
        } 
        if (content.indexOf("18+") !== -1  && alc) {
            div.style.display = 'none';
        } 
    }

    for (let x = 1; x < divs.length; x++) {
        const div = divs[x];
        const content = div.textContent.trim();
    }
}