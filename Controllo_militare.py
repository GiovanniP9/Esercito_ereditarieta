from cavalleria import Cavalleria
from fanteria import Fanteria
from supportoLogistico import Supporto_logistico
from ricognizione import Ricognizione
from artiglieria import Artiglieria
from esercito import Esercito

# Definizione della classe Controllo_militare 
class Controllo_militare:
    def __init__(self):
        self.eserciti = {} # Dizionario per memorizzare gli eserciti registrati

    def crea_esercito(self, nome_esercito): # Metodo per creare un nuovo esercito
        esercito = Esercito(nome_esercito)

        # Creazione di unità di esempio
        unita1 = Fanteria("Fanteria 1", 100) 
        unita2 = Cavalleria("Cavalleria 1", 50)
        unita3 = Supporto_logistico("Supporto 1", 30)
        unita4 = Ricognizione("Ricognizione 1", 20)
        unita5 = Artiglieria("Artiglieria 1", 40)

        esercito.aggiungi_unita(unita1)
        esercito.aggiungi_unita(unita2)
        esercito.aggiungi_unita(unita3)
        esercito.aggiungi_unita(unita4)
        esercito.aggiungi_unita(unita5)
        
        self.eserciti[nome_esercito] = esercito # Aggiunta dell'esercito al dizionario
        print(f"Esercito '{nome_esercito}' creato.")
    

    def mostra_eserciti(self): # Metodo per mostrare gli eserciti registrati
        print("\nEserciti registrati:")
        for nome_esercito in self.eserciti:
            print(f"- {nome_esercito}")
    
    def mostra_unita_esercito(self, nome_esercito): # Metodo per mostrare le unità di un esercito specifico
        if nome_esercito in self.eserciti:
            self.eserciti[nome_esercito].mostra_unita()
        else:
            print(f"Esercito '{nome_esercito}' non trovato.")
    
    def attacca_unita_esercito(self, nome_esercito, nome_unita): # Metodo per attaccare un'unità di un esercito specifico
        if nome_esercito in self.eserciti:
            self.eserciti[nome_esercito].attacca_unita(nome_unita)
        else:
            print(f"Esercito '{nome_esercito}' non trovato.")
    
    def ritira_unita_esercito(self, nome_esercito, nome_unita): # Metodo per ritirare un'unità di un esercito specifico
        if nome_esercito in self.eserciti:
            self.eserciti[nome_esercito].ritira_unita(nome_unita)
        else:
            print(f"Esercito '{nome_esercito}' non trovato.")
    
    def muovi_unita_esercito(self, nome_esercito): # Metodo per muovere tutte le unità di un esercito specifico
        if nome_esercito in self.eserciti:
            self.eserciti[nome_esercito].muovi_tutte()
        else:
            print(f"Esercito '{nome_esercito}' non trovato.")
