def standaardprijs (afstandKM):
    'berekent de prijs van je rit in KM'
    if afstandKM > 50:
        return 15 + (0.60*afstandKM)
    elif afstandKM <= 50 and afstandKM>0:
        return 0.80 * afstandKM
    elif afstandKM <= 0:
        return 0

def ritprijs(leeftijd, weekendrit, afstandKM):
    'berekent de korting'
    if weekendrit == True and (leeftijd >=65 or leeftijd <= 12):
        return float(standaardprijs(afstandKM)) *0.65
    elif weekendrit == True and (leeftijd <65 or leeftijd > 12):
        return float(standaardprijs(afstandKM)) * 0.60
    elif weekendrit == False and (leeftijd >=65 or leeftijd <= 12):
        return standaardprijs(afstandKM) * 0.7
    else:
        return standaardprijs(afstandKM)

print(standaardprijs(50))
print(ritprijs(12, True, 50))