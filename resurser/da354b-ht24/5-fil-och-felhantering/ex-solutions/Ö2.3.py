def divide_numbers(numerator, denominator):
    '''
    Funktionen delar två tal och returnerar resultatet
    '''
    while True:
        try:
            result = numerator / denominator
            return result
        except ZeroDivisionError:
            print("Du kan inte dela med noll. Försök igen.")
            denominator = float(input("Skriv in en ny nämnare: "))


def main():
    '''
    Huvudfunktionen i programmet.
    '''
    while True:
        numerator = float(input("Ange täljaren: "))
        denominator = float(input("Ange nämnaren: "))
        result = divide_numbers(numerator, denominator)
        print("Resultatet av divisionen är:", result, "\n")


main()
