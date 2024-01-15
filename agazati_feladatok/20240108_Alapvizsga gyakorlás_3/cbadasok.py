from cbadas import CBadás

cbadasok : list[CBadás] = []

def beolvas(fajlnev: str):
    fajl = open(fajlnev, 'r', encoding='utf8')
    fajl.readline()
    for sor in fajl:
        cbadasok.append(CBadás(sor.strip()))
    fajl.close()

def bejegyzesek_szama(nev:str) -> int:
    darab = 0
    for c in cbadasok:
        if c.Nev == nev:
            darab += 1 
    return darab

def legtobb_adas() -> int:
    legtobb = cbadasok[0].adasdb 
    for c in cbadasok:
        if c.adasdb > legtobb:
            legtobb = c.adasdb
    return legtobb

def mentes(fajlnev:str):
    fajl = open(fajlnev, 'w', encoding='utf8')
    fajl.write('Kezdes;Nev;AdasDb\n')
    for c in cbadasok:
        perc = c.ora * 60 + c.perc
        fajl.write(f'{perc};{c.Nev};{c.adasdb}\n')
    fajl.close()