def calculate_time(hours, minutes):
    """Räknar ut rätt tid utifrån antal timmar och minuter.

    Parametrar:
    hours (str): Antal timmar.
    minutes (str): Antal minuter.

    Returnerar:
    tuple: Ett tupel med antal timmar och minuter om allt går bra.
    None: Om något går fel och tiden är försvunnen i tiden.    
    """
    try:
        total_minutes = int(hours) * 60 + int(minutes)
        return total_minutes // 60, total_minutes % 60
    except ValueError:
        return None


def main():
    """Huvudprogrammet som hanterar användarinteraktion och anropar calculate_time."""
    print("Välkommen till Fångad i tid!")

    while True:
        hours = input("Ange antal timmar: ")
        if hours.lower() == "stop":
            break
        minutes = input("Ange antal minuter: ")
        if minutes.lower() == "stop":
            break

        result = calculate_time(hours, minutes)
        if result is not None:
            print("Rätt tid är:", result[0],
                  "timmar och", result[1], "minuter")
        else:
            print("Tiden är försvunnen i tiden!")

        print()

    print("Tack för att du använt Fångad i tid!")


# Kör programmet
main()
