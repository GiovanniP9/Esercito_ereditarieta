from esercito import Esercito
from unitaMilitare import Unita_militare
from cavalleria import Cavalleria
from fanteria import Fanteria
from supportoLogistico import Supporto_logistico
from ricognizione import Ricognizione
from artiglieria import Artiglieria

class Controllo_militare(Esercito, Fanteria, Cavalleria, Supporto_logistico, Ricognizione, Artiglieria):
    def __init__(self):
        self.unita_registrate = {}
        
    def aggiungi_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità {unita.nome} aggiunta al controllo militare.")
    
    def mostra_unita(self):
        for nome, unita in self.unita_registrate.items():
            print(f"Nome: {nome}, Numero: {unita.numero_soldati}")
   
    def dettagli_unita(self, nome):
        if nome in self.unita_registrate:
            unita = self.unita_registrate[nome]
            return f"Nome: {unita.nome}, Numero Soldati: {unita.numero_soldati}"
        else:
            return "Unità non trovata."

unita1 = Fanteria("Fanteria 1", 100)
unita2 = Cavalleria("Cavalleria 1", 50)
unita3 = Supporto_logistico("Supporto 1", 30)
unita4 = Ricognizione("Ricognizione 1", 20)
unita5 = Artiglieria("Artiglieria 1", 40)


controllo = Controllo_militare()
controllo.aggiungi_unita(unita1)
controllo.aggiungi_unita(unita2)
controllo.aggiungi_unita(unita3)
controllo.aggiungi_unita(unita4)
controllo.aggiungi_unita(unita5)

controllo.mostra_unita()
controllo.dettagli_unita("Fanteria 1")
controllo.dettagli_unita("Cavalleria 1")
controllo.dettagli_unita("Supporto 1")
controllo.dettagli_unita("Ricognizione 1")
controllo.dettagli_unita("Artiglieria 1")
