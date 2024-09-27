class Libro:
    def __init__(self, titolo, autore, anno):#costruttore
        if type(titolo) is str and type(autore) is str and type(anno) is int:#controllo tipo
          self.titolo= titolo
          self.autore= autore
          self.anno=anno
        elif type(anno)!=int:
           print("Pagine deve avere un numero (intero)")
        else:
           print("Dati errati")
    def descrizione(self):#metodo per stampare info
       try:
         print("Il libro ",self.titolo," scritto da ",self.autore, " è stato scritto nel ",self.anno)
       except:
          print("Operazione non valida")
class Biblioteca:
    archivio=[]
    def aggiungi_libro(self,libro):
        if type(libro)is Libro:
          try:
            self.archivio.append(libro)
          except:
            print("Errore sconosciuto")
        else:
            print("Le biblioteche hanno solo libri!")
    def elimina_libro(self,titolo_scelto):
        x=False
        for libro in self.archivio:
         if titolo_scelto==libro.titolo:
          try:
            self.archivio.remove(libro)
            x=True
          except:
            print("Errore sconosciuto")
         else:
            continue
        if x==False:
           print('Titolo non trovato')
    def mostra_libro (self,titolo_scelto):
        x=False
        for libro in self.archivio:
         if titolo_scelto==libro.titolo:
          try:
            libro.descrizione()
            x=True
          except:
            print("Errore sconosciuto")
         else:
            continue
        if x==False:
           print('Titolo non trovato')
    def mostra_archivio(self):
        if len(self.archivio)==0:
           print('Archivio vuoto')
        else:
          print("Archivio completo:\n")
          for libro in self.archivio:
            libro.descrizione()
    


biblioteca1 = Biblioteca()#come inizializzazione lista (vuota)
while True:
    mod = int(input('Cosa vuoi fare? 1.Aggiungere nuovo Libro 2.Mostra Archivio 3.Cerca Libro (per titolo) 4.Elimina Libro (per titolo) 5.Esci'))
    if mod == 1:
        print("Inserimento nuovo libro\n")
        titolo = input('Inserisci titolo: ')
        autore = input('inserisci autore: ')
        anno = int(input('Inserisci anno di pubblicazione: '))
        book= Libro(titolo,autore,anno)
        biblioteca1.aggiungi_libro(book)
    elif mod == 2:
        biblioteca1.mostra_archivio()
    elif mod == 3:
        titolo_mostrato=input("Indica il titolo da mostrare:\n")
        biblioteca1.mostra_libro(titolo_mostrato)
    elif mod == 4:
        titolo_eliminato=input("Indica il titolo da eliminare:\n")
        biblioteca1.elimina_libro(titolo_eliminato)
    elif mod == 5:
        break
    else:
        print('Scelta non valida')