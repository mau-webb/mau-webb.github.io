def get_fahrenheit():
    '''
    Hämtar antal fahrenheit från användaren

    Returns:
        float : Antal grader i fahrenheit
    '''
    while True:
        try:
            fahrenheit = float(input('Antal grader i fahrenheit: '))
            return fahrenheit
        except:
            print("Du måste mata in siffror")
            continue

def fahrenheit_to_celcius():
    '''
    Konverterar fahrenheit till celcius
    '''
    fahrenheit = get_fahrenheit()
    celcius = (fahrenheit - 32.0) * 5.0 / 9.0
    print(f"Det är : {celcius} grader i celcius")

# Kör programmet
fahrenheit_to_celcius()
