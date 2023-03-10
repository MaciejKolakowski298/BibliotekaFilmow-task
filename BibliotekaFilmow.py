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

F1=Filmy('Pulp Fiction', 1994, 'sensacja', 0)
F2=Filmy('Rambo', 1984, 'dramat', 0)
F3=Filmy('Commando', 1983, 'sensacja', 0)
F4=Filmy('Akademia Policyjna', 1985, 'komedia', 0)
F5=Filmy('Mamma Mia', 2008, 'musical', 0)
S1=Seriale('Friends', 1995, 'komedia', 0, 1, 1 )
S2=Seriale('Friends', 1995, 'komedia', 0, 2, 1 )
S3=Seriale('Friends', 1995, 'komedia', 0, 3, 1 )
S4=Seriale('Alternatywy 4', 1986, 'komedia', 0, 1, 1 )
S5=Seriale('Alternatywy 4', 1986, 'komedia', 0, 2, 1 )
S6=Seriale('Chyłka', 2015, 'sensacja', 0, 1, 1 )
S7=Seriale('Chyłka', 2015, 'sensacja', 0, 2, 1 )

#F1.play()
#F1.play()
#F5.play()

#print(F1.liczba_wyswietlen)
#print(F5.liczba_wyswietlen)


#S1.play()
#S4.play()
#S6.play()

#print (Filmy.lista)

def get_movies(lst):
    result=[]
    for item in lst:
        if not isinstance(item,Seriale):
            result.append(item)
            
    return sorted(result,key=lambda item: item.tytul)

#print (get_movies(Filmy.lista))

def get_series(lst):
    result=[]
    for item in lst:
        if isinstance(item,Seriale):
            result.append(item)
            
    return sorted(result,key=lambda item: item.tytul)

#print(get_series(Filmy.lista))

def search(lst,tytul):
    result=[]
    for item in lst:
        if item.tytul==tytul:
            result.append(item)
    if result:
        return result
    else:
        return 'Nie ma takiego fimu na liście'

#print (search(Filmy.lista,'Commando'))
#print (search(Filmy.lista,'Robocop'))

def generate_views(lst):
    import random
    hit=random.choice(lst)
    hit.liczba_wyswietlen+=random.randint(1,100)
    return hit.tytul, hit.liczba_wyswietlen

#print (generate_views(Filmy.lista))

def generate_10(lst):
    for i in range (10):
        print (generate_views(lst))

generate_10(Filmy.lista)

def top_titles(lst,limit):
    return sorted(lst, key=lambda item: item.liczba_wyswietlen, reverse=True)[:limit]

print (top_titles(Filmy.lista,3))

