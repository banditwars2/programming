def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    lines = infile.readlines()
    aantalkluizenvrij = 12 - len(lines)
    infile.close()
    return str(aantalkluizenvrij)

def nieuwe_kluis():
    kluisnummer = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    regelslezen = open('kluizen.txt', 'r')

    for regel in regelslezen:
        regelsgesplitst = regel.split(';')
        kluisnummer.remove(regelsgesplitst[0])
    regelslezen.close()
    if len(kluisnummer) != 0:
        wachtwoord = input('Typ hier de kluiscode voor uw kluis in: ')
        if len(wachtwoord) < 4:
            print('Uw wachtwoord is te kort, deze moet minimaal 4 tekens lang zijn!')
        else:
            outfile = open('kluizen.txt', 'a')
            s = kluisnummer[0] + '; ' + wachtwoord + '\n'
            outfile.write(s)
            outfile.close()
            print('U heeft kluisnummer: ' + kluisnummer[0])
    else:
        print('Er zijn helaas geen kluisjes meer beschikbaar!')

def kluis_openen():
    kluisnummer = input('Wat is uw kluisnummer? ')
    wachtwoord = input('Wat is uw kluiscode? ')
    checker = kluisnummer + '; ' + wachtwoord
    infile = open('kluizen.txt', 'r')
    combinaties = infile.read()
    infile.close()
    if checker in combinaties:
        print('U heeft de juiste combinatie ingevoerd!')
    else:
        print('De combinatie van kluisnummer en kluiscode is niet juist!')

print('1: Ik wil weten hoeveel kluizen er nog beschibaar zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil iets uit mijn kluis halen')

MenuKeuze = (input('\nWelke optie wilt u gebruik van maken? '))

if MenuKeuze not in '123':
    print('Dit is geen optie')

else:
    IntMenuKeuze = int(MenuKeuze)

    if IntMenuKeuze == 1:
        print('Er zijn nog ' + toon_aantal_kluizen_vrij() + ' kluizen vrij.')

    elif IntMenuKeuze == 2:
        nieuwe_kluis()

    elif IntMenuKeuze == 3:
        kluis_openen()

    else:
        print('Dit is geen optie')