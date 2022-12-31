class Filmy:
    lista=[]
    def __init__(self, tytul, rok_wydania, gatunek, liczba_wyswietlen):
        self.tytul=tytul
        self.rok_wydania=rok_wydania
        self.gatunek=gatunek
        self.liczba_wyswietlen=liczba_wyswietlen
        Filmy.lista.append (self)
        
    def play(self):
        self.liczba_wyswietlen+=1
        print (f"{self.tytul}, {self.rok_wydania}")
        
    def __repr__(self):
        return f"Film ({self.tytul},{self.rok_wydania}, {self.liczba_wyswietlen})"

class Seriale(Filmy):
    def __init__(self, tytul, rok_wydania, gatunek, liczba_wyswietlen, numer_odcinka, numer_sezonu):
        super().__init__(tytul, rok_wydania, gatunek, liczba_wyswietlen)
        self.numer_odcinka=numer_odcinka
        self.numer_sezonu=numer_sezonu
                
    def play(self):
        self.liczba_wyswietlen=+1
        print(f"{self.tytul}, S{self.numer_sezonu:02d}E{self.numer_odcinka:02d}")
        
    def __repr__(self):
        return f"Serial ({self.tytul},{self.rok_wydania}, S{self.numer_sezonu:02d}E{self.numer_odcinka:02d}, {self.liczba_wyswietlen})"