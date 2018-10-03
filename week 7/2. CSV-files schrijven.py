from datetime import datetime
import csv


qs = {
    'wat is je achternaam ': None,
    'Wat zijn je voorletters ': None,
    'Wat is je geboortedatum ': None,
    'Wat is je e-mail adres ': None
}

current_date = datetime.today().strftime("%a %d %b %Y")
current_time = datetime.today().strftime("%H:%M")
formatted_date = current_date + ' at ' + current_time

while True:
    lst = []
    with open('people.csv', 'a', newline='') as f:
        file_writer = csv.writer(f, delimiter=';', )
        for q, a in qs.items():
            v = input(q)
            if v.lower() == 'einde':
                exit()
            lst.append(v)

        file_writer.writerow([formatted_date] + lst)

        f.close()