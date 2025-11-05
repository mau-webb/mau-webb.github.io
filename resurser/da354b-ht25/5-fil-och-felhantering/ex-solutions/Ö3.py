def main():
    """Huvudfunktionen i programmet som hantera välkomnande av användaren,
    inläsning av filmer från vår textfil "movies.text" samt menyn i programmet."""
    # 1. Skriva ut en välkomstfras
    welcome()

    # 2. Läsa in alla filmer från en text-fil
    movies = read_movies_from_file("movies.txt")

    # 3. Skriver ut menyn - och beroende på vad användaren väljer - visar/lägger till/tar bort filmer (eller avslutar programmet)
    while True:
        print_menu()
        user_choice = input("Ange val: ")

        if user_choice == "1":
            print_movies(movies)
        elif user_choice == "2":
            add_movie(movies)
        elif user_choice == "3":
            delete_movie(movies)
        elif user_choice == "4":
            search_movie(movies)
        elif user_choice == "5":
            save_movies_to_file("movies.txt",movies)
        elif user_choice == "0":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen.")

def save_movies_to_file(file_name, movies):
    """Sparar våra filmer till given fil

    Args:
        file_name (str) : Sökvägen till den fil som ska användas
        movies (list) : En lista innehållandes lexikon (filmer) som ska sparas
    """
    my_file = open(file_name, "w")
    for movie in movies:
        my_file.write(f"{movie['title']};{movie['year']};{movie['director']}\n")
    my_file.close()
    print("\nFilmnerna är nu sparade i filen!")

def search_movie(movies):
    """Söker efter filmer i vår filmsamling

    Args:
        movies (list) : En lista innehållandes lexikon (filmer) som ska sparas
    """
    search_movie_title = input("\nAnge söksträng: ")

    result = []
    for movie in movies:
        if search_movie_title in movie["title"]:
            result.append(movie)

    if len(result) > 0:
        print_movies(result)
    else:
        print("Ingen film i samlingen matchade din söksträng")

def delete_movie(movies):
    """Tar bort en film från vår filmlista

    Args:
        movies (list) : En lista innehållandes lexikon (filmer)
    """
    while True:
        title_to_delete = input("\nVilken film vill du ta bort? ")
        for movie in movies:
            if title_to_delete == movie["title"]:
                movies.remove(movie)
                print(f"Vi har tagit bort filmen: {title_to_delete}")
                return # Avsluta            
        print("Filmen du ville ta bort finns inte i filmsamlingen")
        again = input("Vill du ange en annan titel (ja/nej)? ")
        if again.lower() == "nej":
            break

def add_movie(movies):
    """Lägger till en film i vår filmlista

    Args:
        movies (list) : En lista innehållandes lexikon (filmer)
    """
    print("\nLägg till en film")
    print("-"*40)
    movie = {}
    movie["title"] = input("Titel: ")
    movie["year"] = input("År: ")
    movie["director"] = input("Regissör: ")
    
    movies.append(movie)


def print_movies(movies):
    """Skriver ut alla filmerna i vår filmslista

    Args:
        movies (list) : En lista innehållandes lexikon (filmer)
    """
    print("\n{:<20}{:<6}{:<15}".format("Titel", "År", "Regissör"))
    print("-"*40)
    for movie in movies:
        print(f"{movie['title']:<20}{movie['year']:<6}{movie['director']:<15}")

def print_menu():
    """Skriver ut programmets meny"""
    print("\nMenu")
    print("-"*40)
    print("1) Skriv ut alla filmer")
    print("2) Lägg till en film")
    print("3) Ta bort en film")
    print("4) Sök efter filmer")
    print("5) Spara filmerna till filen")
    print("0) Avsluta")

def read_movies_from_file(file_name):
    """Läsa in filen (file_name) och returnera filmerna som en lista:
    t.ex.
    [
        {
            "title": "Star Wars",
            "year": 1977,
            "director: "George Lucas"
        },
        {
            "title": "Fight club",
            "year": 1999,
            "director": "David Fincher"
        },
    ]

    Args:
        file_name (str) : Namnet på filen vi vill öppna

    Return:
        list : En lista på filmerna som finns i filen
    """
    try:
        my_file = open(file_name, "r")
        data = my_file.read().split("\n")

        movies = []

        for row in data:
            movie_parts = row.split(";")
            if len(movie_parts) == 3:
                movie = {}
                movie["title"] = movie_parts[0]
                movie["year"] = movie_parts[1]
                movie["director"] = movie_parts[2]
                movies.append(movie)

        return movies
    except FileNotFoundError:
        my_file = open(file_name, "w")
        my_file.close()

        return []
    

def welcome():
    """Skriver ut välkomstmeddelande"""
    print("-"*40)
    print("Antons filmsamling")
    print("-"*40)

# Kör vårt program genom funktionen "main"
main()
