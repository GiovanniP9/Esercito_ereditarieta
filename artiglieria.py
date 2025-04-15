from unitaMilitare import Unita_militare

class Artiglieria(Unita_militare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def calibra_artiglieria(self):# Definizione metodo per calibrare l'artiglieria
        print(f"L'unità {self.nome} sta calibrando l'artiglieria con {self.numero_soldati} soldati.")