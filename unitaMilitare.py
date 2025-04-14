class Unita_militare():
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità {self.nome} si sta muovendo con {self.numero_soldati} soldati.")
        
    def attacca(self):
        print(f"L'unità {self.nome} sta attaccando con {self.numero_soldati} soldati.")
        
    def ritira(self):
        print(f"L'unità {self.nome} si sta ritirando.")
     