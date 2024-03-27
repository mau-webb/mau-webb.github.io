// Sparar elementet med id:t "add-hero-form" i variabeln "addHeroForm"
const addHeroForm = document.getElementById("add-hero-form");
// Sparar elementet med id:t "super-heroes" i variabeln "superHeroes"
const superHeros = document.getElementById("super-heroes");
// Sparar element med klassen "delete-hero" i variabeln "delete-hero"
const deleteBtns = document.getElementsByClassName("delete-hero");

function deleteHero(e) {
    /*
        Funktionen tar bort en superhjälte

        e.target refererar till elementet man klickar på:
        <span class="delete-icon">X</span>

        Vi tar sedan bort förälderelementet, d.v.s. det <li>-element
        som innehåller information om superhjälten.
    */
    e.target.parentElement.remove();

    nrOfHeroes(); // Uppdaterar siffran som visar antal hjältar som finns i listan
}

function makeFavoriteHero(e) {
    /*
        Funktionen byter/skapar en favorit superhjälte
    */
    const currentFavorite = document.getElementById("favorite"); // Letar upp nuvarande favorit
    if (currentFavorite !== null) { // Kontrollerar OM det finns en nuvarande favorit
        currentFavorite.removeAttribute("id"); // Tar bort id:t favorit från nuvaraned favorit
    }
    e.target.setAttribute("id", "favorite"); // Sätter id:t till favorite på den superhjälte vi dubbelklickade på
}

function heroInfo(e) {
    /*
        Funktionen visar extra information om superhjälten
    */  
    e.preventDefault(); // Hindrar att den "vanliga" menyn dyker upp när man högerklickar
    const el = e.target; // Sparar elementet vi klickade på (<li>, superhjälten) i variabeln el
    const heroName = el.childNodes[0].textContent; // Hämtar ut superhjältens namn
    const heroOrigin = el.getAttribute("class"); // Hämtar ut superhjältens skapare
    alert(`${heroName} är skapad av: ${heroOrigin}`); // Visar upp informationen i en popup-ruta
}

function addHero(e) {
    /*
        Skapar en ny superhjälte baserat på informationen i formuläret
    */ 
    e.preventDefault(); // Förhindrar standardhändelsen (att formuläret skickas iväg)

    const name = document.getElementById("hero-form-name").value; // Hämta angivet namn från textfäletet i formuläret
    const company = document.getElementById("hero-form-company").value; // Hämtar angiven skapare från drop down-menyn i formuläret

    const newHeroLi = document.createElement("li"); // Skapar ett <li>-element
    const newHeroText = document.createTextNode(name);// Skapar en text-nod innehållandes superhjältens namn
    newHeroLi.appendChild(newHeroText); // Lägger text-noden i <li>-elementet
    newHeroLi.setAttribute("class", company); // Ger <li>-elementet det klassnamn som motsvarar superhjältens skapare
    newHeroLi.addEventListener("dblclick", makeFavoriteHero, false); // När man dubbelklickar på en superhjälte (<li>-element) så görs denna till favorit
    newHeroLi.addEventListener("contextmenu", heroInfo, false); // När man högerklickar på en superhjälte (<li>-element) så visas information om denna.

    const newSpan = document.createElement("span"); // Skapar ett nytt <span>-element
    const newSpanText = document.createTextNode("X"); // Skapar en text-nod innehållandes texten "X"
    newSpan.appendChild(newSpanText); // Lägger text-noden i <span>-elementet
    newSpan.setAttribute("class", "delete-hero"); // Lägger till klassen "delete-hero" till <span>-elementet
    newSpan.addEventListener("click", deleteHero, false); // Lägger till så att funktionen "deleteHero" körs när man klickar på elementet

    newHeroLi.appendChild(newSpan); // Lägger till <span>-elementet i <li>-elementet

    superHeros.appendChild(newHeroLi); // Lägger till <li>-elementet (den nya superhjälten) i vår <ul>-lista av hjältar

    nrOfHeroes(); // Uppdaterar siffran som visar antal hjältar som finns i listan
}



function nrOfHeroes() {
    /*
        Funktionen visar antalet superhjältar som finns i listan genom en siffra
    */
    const nrHeroes = superHeros.children.length; // Räknar antalet superhjältar
    document.getElementById("nr-of-heroes").textContent = nrHeroes; // Skriver ut antalet i elementet med id:t "nr-of-heroes"
}

/*
    Kod som körs när sidan laddas
*/
nrOfHeroes(); // Uppdaterar siffran som visar antal hjältar som finns i listan

addHeroForm.addEventListener("submit", addHero, false); // När man skickar iväg formuläret körs funktionen "addHero"

for (let i = 0; i < deleteBtns.length; i++) {
    deleteBtns[i].addEventListener("click", deleteHero, false); // När man klickar på någon "delete"-knapp så körs funktionen "deleteHero"
}

for (let i = 0; i < superHeros.children.length; i++) {
    superHeros.children[i].addEventListener("dblclick", makeFavoriteHero, false); // När man dubbelklickar på en superhjälte (<li>-element) så görs denna till favorit
    superHeros.children[i].addEventListener("contextmenu", heroInfo, false); // När man högerklickar på en superhjälte (<li>-element) så visas information om denna.
}
