while (True):
    Input = str(input('Geef een string van vier letters: '))

    if len(Input) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(Input))
        break

    print('{} heeft {} letters'.format(Input, len(Input)))
