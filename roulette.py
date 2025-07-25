import random

def simulazione_roulette(puntata, numero_puntato, tipo_puntata):
    """
    Simula un giro di roulette europea (37 numeri, 0-36).
    
    Args:
        puntata (float): Importo puntato
        numero_puntato (int/str): Numero o tipo di puntata (per puntate speciali)
        tipo_puntata (str): Tipo di puntata:
            - 'numero' (puntata su un numero specifico 0-36)
            - 'rosso'/'nero'
            - 'pari'/'dispari'
            - 'passe'/'manca' (19-36/1-18)
            - 'dozzina' (1-12, 13-24, 25-36)
            - 'colonna' (prima, seconda o terza colonna)
    
    Returns:
        tuple: (numero_usicto, vincita, esito)
               dove esito è True se vinto, False altrimenti
    """
    # Numeri rossi nella roulette europea
    numeri_rossi = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    
    # Genera un numero casuale 0-36
    numero_uscito = random.randint(0, 36)
    
    # Determiniamo il colore (0 non ha colore)
    colore = None
    if numero_uscito != 0:
        colore = 'rosso' if numero_uscito in numeri_rossi else 'nero'
    
    # Controlliamo la vincita in base al tipo di puntata
    vincita = 0
    esito = False
    
    if tipo_puntata == 'numero':
        if numero_uscito == numero_puntato:
            vincita = puntata * 36
            esito = True
    elif tipo_puntata in ['rosso', 'nero']:
        if colore == tipo_puntata:
            vincita = puntata * 2
            esito = True
    elif tipo_puntata == 'pari':
        if numero_uscito != 0 and numero_uscito % 2 == 0:
            vincita = puntata * 2
            esito = True
    elif tipo_puntata == 'dispari':
        if numero_uscito % 2 == 1:
            vincita = puntata * 2
            esito = True
    elif tipo_puntata == 'passe':
        if 19 <= numero_uscito <= 36:
            vincita = puntata * 2
            esito = True
    elif tipo_puntata == 'manca':
        if 1 <= numero_uscito <= 18:
            vincita = puntata * 2
            esito = True
    elif tipo_puntata == 'dozzina':
        if (numero_puntato == 1 and 1 <= numero_uscito <= 12) or \
           (numero_puntato == 2 and 13 <= numero_uscito <= 24) or \
           (numero_puntato == 3 and 25 <= numero_uscito <= 36):
            vincita = puntata * 3
            esito = True
    elif tipo_puntata == 'colonna':
        # Le colonne sono i numeri con lo stesso resto nella divisione per 3
        # Colonna 1: 1, 4, 7,..., 34
        # Colonna 2: 2, 5, 8,..., 35
        # Colonna 3: 3, 6, 9,..., 36
        if numero_uscito != 0 and (numero_uscito % 3) == (numero_puntato % 3):
            vincita = puntata * 3
            esito = True
    
    return numero_uscito, vincita, esito

# Esempi di utilizzo
# if __name__ == "__main__":
# # Esempi di utilizzo per ogni tipo di puntata
#     print("=== SIMULATORE ROULETTE ===")
#     print("(Roulette Europea - Singolo Zero)\n")

#     # 1. Puntata su numero specifico (paga 35:1)
#     num_puntato = 17
#     importo = 10
#     print(f"1. Puntata €{importo} sul numero {num_puntato}")
#     risultato = simulazione_roulette(importo, num_puntato, 'numero')
#     print(f"   Numero uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # # 2. Puntata sul rosso (paga 1:1)
#     # importo = 20
#     # print(f"2. Puntata €{importo} sul rosso")
#     # risultato = simulazione_roulette(importo, None, 'rosso')
#     # colore = 'rosso' if risultato[0] in numeri_rossi else 'nero' if risultato[0] != 0 else 'zero'
#     # print(f"   Uscito: {risultato[0]} ({colore}) - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # # 3. Puntata sul nero (paga 1:1)
#     # importo = 15
#     # print(f"3. Puntata €{importo} sul nero")
#     # risultato = simulazione_roulette(importo, None, 'nero')
#     # colore = 'rosso' if risultato[0] in numeri_rossi else 'nero' if risultato[0] != 0 else 'zero'
#     # print(f"   Uscito: {risultato[0]} ({colore}) - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 4. Puntata sul pari (paga 1:1)
#     importo = 25
#     print(f"4. Puntata €{importo} sul pari")
#     risultato = simulazione_roulette(importo, None, 'pari')
#     print(f"   Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 5. Puntata sul dispari (paga 1:1)
#     importo = 25
#     print(f"5. Puntata €{importo} sul dispari")
#     risultato = simulazione_roulette(importo, None, 'dispari')
#     print(f"   Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 6. Puntata sul passe (19-36, paga 1:1)
#     importo = 30
#     print(f"6. Puntata €{importo} sul passe (19-36)")
#     risultato = simulazione_roulette(importo, None, 'passe')
#     print(f"   Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 7. Puntata sul manca (1-18, paga 1:1)
#     importo = 30
#     print(f"7. Puntata €{importo} sul manca (1-18)")
#     risultato = simulazione_roulette(importo, None, 'manca')
#     print(f"   Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 8. Puntata sulla prima dozzina (1-12, paga 2:1)
#     importo = 15
#     dozzina = 1
#     print(f"8. Puntata €{importo} sulla {dozzina}° dozzina (1-12)")
#     risultato = simulazione_roulette(importo, dozzina, 'dozzina')
#     print(f"   Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 9. Puntata sulla seconda dozzina (13-24, paga 2:1)
#     importo = 15
#     dozzina = 2
#     print(f"9. Puntata €{importo} sulla {dozzina}° dozzina (13-24)")
#     risultato = simulazione_roulette(importo, dozzina, 'dozzina')
#     print(f"   Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 10. Puntata sulla terza dozzina (25-36, paga 2:1)
#     importo = 15
#     dozzina = 3
#     print(f"10. Puntata €{importo} sulla {dozzina}° dozzina (25-36)")
#     risultato = simulazione_roulette(importo, dozzina, 'dozzina')
#     print(f"    Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 11. Puntata sulla prima colonna (1,4,7,...,34, paga 2:1)
#     importo = 20
#     colonna = 1
#     print(f"11. Puntata €{importo} sulla {colonna}° colonna")
#     risultato = simulazione_roulette(importo, colonna, 'colonna')
#     print(f"    Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 12. Puntata sulla seconda colonna (2,5,8,...,35, paga 2:1)
#     importo = 20
#     colonna = 2
#     print(f"12. Puntata €{importo} sulla {colonna}° colonna")
#     risultato = simulazione_roulette(importo, colonna, 'colonna')
#     print(f"    Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!\n")

#     # 13. Puntata sulla terza colonna (3,6,9,...,36, paga 2:1)
#     importo = 20
#     colonna = 3
#     print(f"13. Puntata €{importo} sulla {colonna}° colonna")
#     risultato = simulazione_roulette(importo, colonna, 'colonna')
#     print(f"    Uscito: {risultato[0]} - Vincita: €{risultato[1]} - {'' if risultato[2] else 'Non '}Hai vinto!")