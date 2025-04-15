from cavalleria import Cavalleria
from fanteria import Fanteria
from supportoLogistico import Supporto_logistico
from ricognizione import Ricognizione
from artiglieria import Artiglieria

class Esercito:
    def __init__(self, nome):
        self.nome = nome
        self.unita_registrate = {}

    def aggiungi_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità {unita.nome} aggiunta all'esercito '{self.nome}'.")

    def mostra_unita(self):
        print(f"\nUnità nell'esercito '{self.nome}':")
        for nome, unita in self.unita_registrate.items():
            print(f"Nome: {nome}, Numero Soldati: {unita.numero_soldati}")

    def attacca_unita(self, nome):
        if nome in self.unita_registrate:
            self.unita_registrate[nome].attacca()
        else:
            print(f"Unità '{nome}' non trovata nell'esercito '{self.nome}'.")

    def ritira_unita(self, nome):
        if nome in self.unita_registrate:
            self.unita_registrate[nome].ritira()
        else:
            print(f"Unità '{nome}' non trovata nell'esercito '{self.nome}'.")

    def muovi_tutte(self):
        print(f"L'esercito '{self.nome}' sta muovendo tutte le unità:")
        for unita in self.unita_registrate.values():
            unita.muovi()
            
        