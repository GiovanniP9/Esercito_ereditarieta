from cavalleria import Cavalleria
from fanteria import Fanteria
from supportoLogistico import Supporto_logistico
from ricognizione import Ricognizione
from artiglieria import Artiglieria
from unitaMilitare import Unita_militare

# Definizione della classe Esercito
class Esercito:
    def __init__(self, nome):
        self.nome = nome
        self.unita_registrate = {} # Dizionario per memorizzare le unità registrate nell'esercito

    def aggiungi_unita(self, unita): # Metodo per aggiungere un'unità all'esercito
        self.unita_registrate[unita.nome] = unita
        print(f"Unità {unita.nome} aggiunta all'esercito '{self.nome}'.")

    def mostra_unita(self): # Metodo per mostrare tutte le unità registrate nell'esercito
        print(f"\nUnità nell'esercito '{self.nome}':")
        for nome, unita in self.unita_registrate.items():
            print(f"Nome: {nome}, Numero Soldati: {unita.numero_soldati}")

    def attacca_unita(self, nome): # Metodo per attaccare un'unità specifica
        if nome in self.unita_registrate:
            self.unita_registrate[nome].attacca()
        else:
            print(f"Unità '{nome}' non trovata nell'esercito '{self.nome}'.")

    def ritira_unita(self, nome): # Metodo per ritirare un'unità specifica
        if nome in self.unita_registrate:
            self.unita_registrate[nome].ritira()
        else:
            print(f"Unità '{nome}' non trovata nell'esercito '{self.nome}'.")

    def muovi_tutte(self): # Metodo per muovere tutte le unità registrate nell'esercito
        print(f"L'esercito '{self.nome}' sta muovendo tutte le unità:")
        for unita in self.unita_registrate.values():
            unita.muovi()
            
        