from unitaMilitare import Unita_militare

class Fanteria(Unita_militare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def costruisci_trincea(self):
        print(f"L'unità {self.nome} sta costruendo una trincea.")