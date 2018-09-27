FileOpen = open('Kaartnummers.txt', 'r')

for line in FileOpen:
    line = line.split(",")
    inhoud = '{} heeft kaartnummer: {}'
    print(inhoud.format(line[1].rstrip(), line[0]))