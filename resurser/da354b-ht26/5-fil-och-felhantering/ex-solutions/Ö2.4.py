def add_numbers(num_1, num_2):
    """Adderar två tal och returnerar resultatet.

    Parametrar:
    num_1 (str): Det första talet.
    num_2 (str): Det andra talet.

    Returnerar:
    int: Resultatet av additionen om allt går bra.
    None: Om inmatningen inte är giltig.
    """
    try:
        result = int(num_1) + int(num_2)
        return result
    except ValueError:
        return None


def main():
    """Huvudfunktionen som hanterar inmatning och anropar funktionen add_numbers."""
    print("Välkommen till Slarviga Kalkylatorn!")

    while True:
        num_1 = input(
            "Mata in det första talet (eller 'Stop' för att avsluta): ").lower()
        if num_1 == "stop":
            break

        num_2 = input(
            "Mata in det andra talet (eller 'Stop' för att avsluta): ").lower()
        if num_2 == "stop":
            break

        result = add_numbers(num_1, num_2)
        if result is not None:
            print("Resultatet av additionen är:", result)
        else:
            print("Oops! Något gick fel. Prova med riktiga siffror.")

        print()  # Lägg till en blankrad

    print("Tack för att du använde Slarviga Kalkylatorn!")


# Kör programmet
if __name__ == "__main__":
    main()
