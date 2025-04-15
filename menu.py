from    Controllo_militare import Controllo_militare

def menu():
    controllo = Controllo_militare()
    # Menu principale del simulatore di battaglia - Implementare la gestione degli eserciti, delle unità, delle azioni, ecc.
    print("\nBenvenuto nel simulatore di battaglia!")
    while True: 
        print("1. Crea un esercito")
        print("2. Mostra gli eserciti")
        print("3. Mostra le unità di un esercito")
        print("4. Esegui un'azione su un esercito")
        print("5. Esci")
        
        scelta = input("Cosa vuoi fare? (1/2/3/4/5): ")
        
        match scelta:
            case "1":
                nome_esercito = input("Inserisci il nome dell'esercito: ")
                controllo.crea_esercito(nome_esercito)
            
            case "2":
                controllo.mostra_eserciti()
            
            case "3":
                nome_esercito = input("Scegli l'esercito: ")
                controllo.mostra_unita_esercito(nome_esercito)
            
            case "4":
                nome_esercito = input("Scegli l'esercito: ")
                azione = input("Scegli l'azione (muovi/attacca/ritira): ")
                nome_unita = input("Scegli l'unità: ")
                
                match azione:
                    case "muovi":
                        controllo.muovi_unita_esercito(nome_esercito)
                    case "attacca":
                        controllo.attacca_unita_esercito(nome_esercito, nome_unita)
                    case "ritira":
                        controllo.ritira_unita_esercito(nome_esercito, nome_unita)
                    case _:
                        print("Azione non valida!")
            
            case "5":
                print("Esci dal simulatore.")
                break
            
            case _:
                print("Opzione non valida!")

if __name__ == "__main__":
    menu()
