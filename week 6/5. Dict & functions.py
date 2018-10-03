namen: dict = {}

while True:
    naam = input("Voeg een naam toe ")

    if naam == '':
        for naam in namen:
            print("Er zijn " + str(namen[naam]) + " studenten met de naam " + str(naam))
        break
    elif naam in namen:
        namen[naam] += 1
    else:
        namen[naam] = 1