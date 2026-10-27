print("Ange fem bra böcker")

# Öppnar filen i skrivläge
my_file = open("books.txt", "w")

for i in range(1, 6):
    book = input(f"Bok {i}: ")
    my_file.write(f"{book}\n") # Viktigt med \n för att skapa en radbrytning

my_file.close()
