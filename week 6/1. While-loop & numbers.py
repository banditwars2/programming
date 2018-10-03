ReeksSoms = []
Input = 1
while Input >= 0:
    Input = int(input('Geef een getal op: '))

    if Input == 0:
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(ReeksSoms), sum(ReeksSoms)))
        break
    ReeksSoms.append(int(Input))