szo1 = input('Adj meg egy szót: ')
szo2 = input('Adj meg egy másik szót: ')
if len(szo1) > len(szo2):
    print(f'{szo1} hosszabb, mint {szo2}')
elif len(szo1) < (szo2):
    print(f'{szo1} rövidebb, mint {szo2}')
else:
    print(f'A két szó ugyanolyan hosszú')