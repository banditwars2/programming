def standaardprijs (afstandKM):
    'berekent de prijs van je rit in KM'
    if afstandKM > 50:
        return 15 + (0.60*afstandKM)
    elif afstandKM <= 50 and afstandKM>0:
        return 0.80 * afstandKM
    elif afstandKM <= 0:
        return 0

print(standaardprijs(50)) #<-geef hier je afstand en dit word dan berekent

def ritprijs(leeftijd, weekendrit, afstandKM):
    'berekent de korting'
    if weekendrit  and (leeftijd >=65 or leeftijd <= 12):
        return float(standaardprijs(afstandKM)) *0.65
    elif weekendrit and (leeftijd <65 or leeftijd > 12):
        return float(standaardprijs(afstandKM)) * 0.60
    elif not weekendrit and (leeftijd >=65 or leeftijd <= 12):
        return standaardprijs(afstandKM) * 0.7
    else:
        return standaardprijs(afstandKM)

print(ritprijs(21, False, 10))
#Je geeft je leeftijd aan, of je op een weekendrit rijdt, en de afstand die je legt
#als je geen weekendrit heb dan gaat berekend hij alleen puur de afstandKM