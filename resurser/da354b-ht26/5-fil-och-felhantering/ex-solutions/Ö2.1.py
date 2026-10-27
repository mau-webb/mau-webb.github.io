try:
    # Försöker öppna filen om den finns
    my_file = open("movies.txt", "r")
    # Splitar strängen på , för att få en lista med filmtitlar
    movies = my_file.read().split(",")
    # Stänger filen
    my_file.close()

    # Skriver ut filerna
    print(", ".join(movies))
except FileNotFoundError:
    # Filen finns inte!
    print("Kunde inte öppna filen, finns den?")
