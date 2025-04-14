from unitaMilitare import Unita_militare

class Ricognizione(Unita_militare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def conduci_ricognizione(self):
        print(f"L'unità {self.nome} sta conducendo una missione di ricognizione con {self.numero_soldati} soldati.")