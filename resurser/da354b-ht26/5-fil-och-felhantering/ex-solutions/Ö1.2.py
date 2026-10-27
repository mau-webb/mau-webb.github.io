# Öppnar filen i läsläge (r = read)
my_file = open("books.txt", "r")
# Läser in böckerna och splittar vid varje radbrytning till en lista
books = my_file.read().split("\n")
# Stänger filen vi jobbar med
my_file.close()

# Skriver ut böckerna (1)
for book in books:
    # Kontrollerar att det inte är en blank rad
    if book != "":
        print(book)

# Skriver ut böckerna (2)
print("\nBöcker i filen:")
for i, book in enumerate(books, start=1):
    # Kontrollerar att det inte är en blank rad
    if book != "":
        print(f"{i}: {book}")
