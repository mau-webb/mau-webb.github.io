def calculate_grade(points):
    '''
    Funktionen beräknar och returnerar betyget baserat på poängsumman
    '''
    if points >= 90:
        return "A"
    elif points >= 80:
        return "B"
    elif points >= 70:
        return "C"
    elif points >= 60:
        return "D"
    elif points >= 50:
        return "E"
    else:
        return "F"


def grade_report():
    '''
    Funktionen beräknar och skriver ut betyget baserat på inmatad poängsumma
    '''
    entered_points = int(input("Ange poängsumma: "))
    grade = calculate_grade(entered_points)
    print("Betyg:", grade)


# Testa betygsberäkning
grade_report()
