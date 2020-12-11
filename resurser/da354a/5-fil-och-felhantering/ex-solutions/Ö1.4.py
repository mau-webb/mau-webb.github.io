def main():
    '''
    Huvudprogrammet som styr körningen av bokhanteringen
    '''
    books = get_books_from_file()
    print_books(books)

    delete_book_from_list(books)
    save_books_to_file(books)

    books = get_books_from_file()
    print_books(books)

def get_books_from_file():
    '''
    Läser in böckerna från text-filen "books.txt" och returnerar en lista med boktitlar

    Returns
        list : En lista på boktitlar
    '''
    my_file = open("books.txt", "r")
    books = my_file.read().split("\n")
    my_file.close()
    return books

def print_books(books):
    '''
    Skriver ut böckerna

    Args:
        books (list) : Listan på böckerna
    '''
    print("\nBöcker")
    print("--------")
    for book in books:
        if book != "":
            print(book)

def delete_book_from_list(books):
    '''
    Frågar användaren efter en bok, och tar bort den från listan

    Args:
        books (list) : Listan på böckerna
    '''
    delete_book = input("\nVilken bok vill du ta bort? ")
    books.remove(delete_book)

def save_books_to_file(books):
    '''
    Sparar böckerna i text-filen "books.txt"

    Args:
        books (list) : Listan på böckerna
    '''
    my_file = open("books.txt", "w")
    for book in books:
        if book != "":
            my_file.write(f"{book}\n")
    my_file.close()
    
# Kör main()
main()
