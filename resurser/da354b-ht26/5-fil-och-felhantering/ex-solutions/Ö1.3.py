while True:
    book = input("Titel på bok: ")

    # Öppnar filen i append (lägg till) läge
    my_file = open("books.txt", "a")
    my_file.write(f"{book}\n")
    my_file.close()

    if input("Vill du lägga till en ny bok (ja/nej) ").lower() == "nej":
        break

# Läser in böckerna från filen
my_file = open("books.txt", "r")
books = my_file.read().split("\n")

print("\nBöcker")
print("--------")
for book in books:
    if book != "":
        print(book)
