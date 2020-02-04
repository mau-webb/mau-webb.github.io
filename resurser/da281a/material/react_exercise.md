---
id: da281a
title: "Övning: React"
---

# Övning: React

**Obs** gå gärna igenom övningen om [Arraymetoder](/{{ site.resource_path }}/da281a/material/array_methods/) innan denna övningen.

[React](https://facebook.github.io/react/index.html) är ett tredjepartsbibliotek för att arbeta med användargränssnitt, skapat av Facebook. Det är idag ett av de mer populära biblioteken som används för detta ändamål inom industrin.

För att använda sig av detta kräver det att vi har tillgång till biblioteket (dvs. JavaScript-filerna) och har skapat en grund med HTML och koppling mellan alla JavaScript-filer. För att ni ska snabbt komma igång med denna övning/introduktion till React [kan ni klicka här för att ladda ner ett "starter-kit"](../assets/react-starter-kit.zip). I denna mapp finner ni `index.html` med allting sammankopplat och klart. Det enda ni behöver göra är att skriva er kod inom `<script type="text/babel">`-taggen.

Denna övning är tänkt att ni ska pröva samtliga exempel och gärna experimentera - det är inte så mycket eget arbete här.

## React och JSX

En intressant aspekt med React som måste nämnas direkt är det faktum att när ni skriver kod för detta bibliotek eller söker via webben kommer ni märka att det blandas HTML- och JavaScript-kod i samma fil, vilket kan anses vara väldigt konstigt. Vad detta egentligen innebär är att när vi skriver HTML-kod med detta bibliotek kommer React i bakgrunden att konvertera detta till JavaScript - så det handlar egentligen om att göra det lättare för oss som utvecklare. React kallar detta för "JSX".

För att kort demonstrera det hela kan vi göra ett trivialt exempel med React.

Den kod som demonstreras i denna övning placerar ni i er `<script>`-tagg.

``` js
// Skapa en komponent
var HelloWorld = React.createClass({
    render: function() {
        return (
            <h1>Hello World!</h1>
        );
    }
});

// Rendera vårt innehåll
ReactDOM.render(
    <HelloWorld />,
    document.getElementById("root")
);
```

Om ni nu besöker `index.html` så bör ni se en huvudrubrik innehållande "Hello World!".

Det som sker här och det som är grunden för React är att vi arbetar med komponenter. I detta exemplet är det ett ganska trivialt exempel - en huvudrubrik. Det kan givetvis bli mer avancerat än så. Värt att notera är att för att skapa en komponent anropar vi `React.createClass()` med ett object (`{}`). Detta objektet måste **minst** ha en metod, nämligen `render()`. Det är i denna som vi returnerar den HTML-kod vi vill ska synas. Här kan ni notera det som kallas "JSX" - att vi blander HTML- och JavaScript-kod.

Den andra delen är det som gör att innehållet faktiskt visas på vår HTML-sida, nämligen att bestämma vilken komponent (HelloWorld i detta fallet) som ska renderas - och vart - i detta fallet elementet som har `id="root"`. Notera även att om vi vill använda oss av vår komponent `var HelloWorld` så skriver vi sedan denna som en HTML-tagg - `<HelloWorld />`. Allt detta kan komma att kännas väldigt konstigt till en början men blir förhoppningsvis snabbt ganska enkelt.

## Dynamiskt innehåll: tillstånd

Det är sällan vi använder oss av React för att presentera statiskt innehåll utan vi vill presentera dynamiskt innehåll, antingen hämtat från en egen databas, en fil eller hämtat från ett externt API. Hur sköts detta i React? Varje komponent i React kan antingen ha ett *tillstånd* (sk. "state") eller egenskaper. Skillnaden mellan dessa är att ett tillstånd kan ändras och egenskaper kan inte. För att först demonstrera hur vi kan lägga till dynamiskt innehåll genom att ange ett tillstånd för en komponent kan ni ta en titt på exemplet nedan:

``` js
var Person = React.createClass({
    // I metoden "getInitialState" beskriver vi komponentens
    // tillstånd genom att returnera ett objekt innehållande
    // den data vi behöver / vill ha
    getInitialState: function() {
        return {
            firstname: "Sherlock",
            lastname: "Holmes"
        };
    },
    render: function() {
        // För att använda oss av den dynamiska datan (tillståndet)
        // hämtar vi det genom `this.state`
        return (
            <p>{this.state.firstname} {this.state.lastname}</p>
        )
    }
});

// Rendera vårt innehåll
ReactDOM.render(
    <Person />,
    document.getElementById("root")
);
```

Vad vi ser i exemplet ovan är att i `render`-metoden så beskriver vi vad vi vill ska presenteras. Dock så är innehållet av detta dynamiskt, det kommer från komponentens tillstånd ("state"). Tillstånd anges i metoden `getInitialState` och görs så genom att returnera ett objekt. För att använda oss av denna data måste vi nyttja `this.state` och för att denna data ska synas måste vi placera denna inom `{ ... }`.

## Dynamiskt innehåll: egenskaper

Hur hade vi löst samma sak fast med egenskaper? Ta en titt på följande exempel:

``` js
var Person = React.createClass({
    render: function() {
        // För att använda oss av egenskaper nyttjar vi istället `this.props`
        return (
            <p>{this.props.firstname} {this.props.lastname}</p>
        )
    }
});

// Rendera vårt innehåll
ReactDOM.render(
    <Person firstname="Sherlock" lastname="Holmes" />,
    document.getElementById("root")
);
```

Här ser vi att egenskaper är som i vanlig HTML-kod, vi anger det som `egenskap="värde"`, detta gör så att värdet finns tillgängligt genom `this.props`.

## Ändra på tillståndet

Hur gör vi för att ändra på ett tillstånd? Eftersom det är dynamiskt måste vi ju kunna ändra på det - ta en titt på exemplet nedan och försök förstå vad som sker:

``` js
var ClickMe = React.createClass({
    // Vårt tillstånd
    getInitialState: function() {
        return {
            text: "Click me!"
        };
    },
    // Vad händer när vi klickar på knappen?
    // Vi ändrar tillståndet genom `setState`
    // genom att skicka med ett nytt objekt
    handleClick: function() {
        this.setState({
            text: "You clicked me!"
        });
    },
    render: function() {
        // Vi kan ange klick-funktioner genom attributet "onClick"
        return (
            <button onClick={this.handleClick} type="button">
                {this.state.text}
            </button>
        )
    }
});

// Rendera vårt innehåll
ReactDOM.render(
    <ClickMe />,
    document.getElementById("root")
);
```

Om ni prövar exemplet ser ni att texten ändras efter vi klickat en gång - detta då vi ändrar på tillståndet och eftersom knappen har tillståndet som text kommer dennas text också att ändras.

## Kombinera flera komponenter

För att gå vidare med React så blir det naturligt att kombinera olika komponenter (tänk att vi bygger en hierarki likt den vi gör med vanlig HTML-kod, som listor osv.). Detta även med extern data, i detta exemplet placerar vi detta i en global data för att demonstrera.

``` js
// Vår data
var people = [
    { firstname: "Sherlock", lastname: "Holmes" },
    { firstname: "John", lastname: "Watson" },
    { firstname: "Jane", lastname: "Doe" }
];

// En person
var Person = React.createClass({
    render: function() {
        return (
            <li>{this.props.firstname} {this.props.lastname}</li>
        )
    }
});

// Lista av personer
var PersonList = React.createClass({
    getInitialState: function() {
        // Stoppar in vår globala variabel i vårt tillstånd
        return {
            people: people
        };
    },
    render: function() {
        // Observera att vi använder Arraymetoden "map" för
        // att gå igenom alla våra personer och för varje person
        // skapa komponenten "Person"
        return (
            <ul>
                {this.state.people.map(function(person) {
                    return (
                        <Person
                            firstname={person.firstname}
                            lastname={person.lastname} />
                    )
                })}
            </ul>
        )
    }
});

// Rendera vårt innehåll
ReactDOM.render(
    <PersonList />,
    document.getElementById("root")
);
```

Värt att notera från ovanstående exempel är att vi använder oss av tillstånd för alla våra personer, eftersom det hade kunna vara så att vi vill lägga till / ta bort. Dock använder vi egenskaper för respektive person (dvs. komponenten) eftersom en persons data inte kommer att ändras (i detta exemplet).

## Exempel med interaktion

Som avslutning för denna övning kommer vi ha ett större exempel där all vår data kommer från filen placerad i `js/albums.js` - ta en titt i er mapp. Denna innehåller några musikalbums, där varje album har ett namn, spotifylänk, omslag osv. Den grundläggande interaktionen vi kommer ha är att en användare ska kunna radera ett album genom att varje album har en knapp "radera".

``` js
var Album = React.createClass({
    render: function() {
        return (
            <div className="album">
                <h2>{this.props.album.name}</h2>
                <a href={this.props.album.href}>Spotify link</a>
                <br />
                <img src={this.props.album.image.url} alt="" />
                <br />
                <button onClick={this.props.onClick} type="button">Remove</button>
            </div>
        )
    }
});

var Albums = React.createClass({
    getInitialState: function() {
        // Notera att variabeln "albums" kommer från
        // vår fil `js/albums.js`
        return {
            albums: albums
        };
    },
    handleClick: function(index) {
        // Radera ett album från listan
        this.state.albums.splice(index, 1);
        // Uppdatera tillståndet med albumen igen
        this.setState({
            albums: this.state.albums
        });
    },
    render: function() {
        // Om vi vill skicka med funktionen handleClick, som ska radera
        // ett album från listan behöver vi dels ange `this` som det
        // andra argumentet i vår "map" metod, samt ange 
        // `this.handleClick.bind(this, index)` för att göra så att vår
        // klick-metod har tillgång till vårt tillstånd samt index för
        // vilket album som blev klickat - så vi vet vilket vi vill radera
        return (
            <div className="albums">
                {this.state.albums.map(function(album, index) {
                    return (
                        <Album
                            album={album}
                            onClick={this.handleClick.bind(this, index)} />
                    )
                }, this)}
            </div>
        )
    }
});

// Rendera vårt innehåll
ReactDOM.render(
    <Albums />,
    document.getElementById("root")
);
```

Om vi vill ange en CSS-klass för ett HTML-element i React måste vi skriva detta som `className=""`
{: .info}

Överlag är det inte mycket nytt i denna delen jämfört med den förra. Den stora skillnaden är interaktionen i form av att kunna radera ett element. Här kräver det en viss förståelse för nyckelordet `this`. Som med mycket annat gäller det att experimentera - hade ni kunnat göra ett formulär så det går att lägga till ett album?

I inlämningsuppgiften för React finner ni även en mängd material att ta del av - gå igenom detta, experimentera på egen hand så bör ni känna er allt säkrare på hur React fungerar i praktiken!
