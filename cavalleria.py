from unitaMilitare import Unita_militare

class Cavalleria(Unita_militare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def esplora_terreno(self): # Aggiunta metodo esplora_terreno
        print(f"L'unità {self.nome} sta esplorando il terreno con {self.numero_soldati} soldati.")