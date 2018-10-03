import random

def monopolyworp(dubbel):
    dobbelsteen1 = random.randint(1, 3)
    dobbelsteen2 = random.randint(1, 3)

    if dobbelsteen1 is dobbelsteen2 and dubbel == 2:
        print('{} + {} = (direct naar gevangenis)'.format(dobbelsteen1, dobbelsteen2))
    elif dobbelsteen1 is dobbelsteen2:
        print('{} + {} = {} (dubbel)'.format(dobbelsteen1, dobbelsteen2, dobbelsteen1 + dobbelsteen2))
        dubbel += 1
        monopolyworp(dubbel)
    elif not dobbelsteen1 is dobbelsteen2:
        print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, dobbelsteen1 + dobbelsteen2))

monopolyworp(0)