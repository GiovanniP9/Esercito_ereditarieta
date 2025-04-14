class Esercito:
    def __init__(self, nome_esercito):
        self.nome_esercito = nome_esercito
        self.unita = {}
    def mostra_unita(self):
        print("Unità dell'esercito:", self.nome_esercito)
        for nome, unita in self.unita.values():
            print(f"Nome: {nome}, Tipo: {unita}")
            
        