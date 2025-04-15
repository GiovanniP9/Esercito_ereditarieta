from unitaMilitare import Unita_militare

class Supporto_logistico(Unita_militare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def rifornisci_unita(self):# Rifornisce le truppe all'unità
        print(f"L'unità {self.nome} sta rifornendo le truppe.")