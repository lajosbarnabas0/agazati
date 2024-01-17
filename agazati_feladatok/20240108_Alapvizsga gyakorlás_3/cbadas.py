class CBadás:
    def __init__(self,sor:str) -> None:
        adatok = sor.split(';')
        self.ora = int(adatok[0])
        self.perc = int(adatok[1])
        self.adasdb = int(adatok[2])
        self.Nev = adatok[3]