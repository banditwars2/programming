import csv


lines = []

with open('gamers.csv', 'r', newline='') as f:
    file_reader = csv.reader(f, delimiter=';', )
    [lines.append(';'.join(row)) for row in file_reader]
    hs = max(lines[-2:]).split(";")

    name = hs[0]
    date = hs[1].replace(" ", "")
    score = hs[2].replace(" ", "")
    print("De hoogste score is: {0}, op {1} behaald door {2}".format(score,date, name))

    f.close()