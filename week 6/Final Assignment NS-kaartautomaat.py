stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam', 'Amsterdam Amstel', 'Utrecht', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_BeginOfEindStation(beginStation, beginStationName):
    'dit kan zowel begin als eindstation inlezen, afhankelijk van de meegegeven boolean beginstation'
    beginEindeString = 'beginstation' if beginStation else 'eindstation'

    while True:
        userInput = str(input('Wat is je {}: '.format(beginEindeString))).lower().capitalize()

        if userInput in stations:
            if beginStation == False and stations.index(userInput) < stations.index(beginStationName):
                print('Dit traject gaat maar in een richting! Kies een ander station')
                continue

            return userInput

        print('Geef een station op dat zich op dit traject bevind!')

def inlezen_eindstation(beginStation, eindStation):
    beginstation = stations.index(beginStation)
    eindstation = stations.index(eindStation)
    stationIndexDiff = eindstation - beginstation
    prijs = stationIndexDiff * 5

    print('Het beginstation {} is het {}e station in het traject.'.format(beginStation, beginstation + 1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindStation, eindstation + 1))
    print('De afstand bedraagt {} station(s).'.format(stationIndexDiff))
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('\nJij stapt de trein in: {}'.format(beginStation))
    print(' - ' + ', '.join(stations[beginstation+1:eindstation]))
    print('Jij stapt uit in: {}'.format(eindStation))

beginStation = inlezen_BeginOfEindStation(True, None)
eindStation = inlezen_BeginOfEindStation(False, beginStation)
inlezen_eindstation(beginStation, eindStation