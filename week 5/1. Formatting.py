def convert(celcius):
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

def table():
    print('{:>3} {:>5}'.format('F', 'C'))
    for celcius in range(-30, 50, 10):
        print('{} {:5}'.format(convert(celcius), celcius))
        
print(table())