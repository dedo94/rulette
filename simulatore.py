from roulette import simulazione_roulette

def gioca(saldo, min_puntata, giri):
    
    tmp_giri = 0
    fibonacci = [1,1,2,3,5,8,13,21,34,55,89]

    turno = 0 
    colonna = 1
    while tmp_giri < giri:
        puntata = min_puntata*fibonacci[turno] 
        if saldo >= puntata :
            risultato = simulazione_roulette(puntata, colonna, 'colonna')
            # print(f"giro: {tmp_giri},turno {turno}, puntata:{puntata}, saldo: {saldo},colonna: {colonna}, esito: {risultato[1]}")
            saldo = saldo - puntata + risultato[1] 
            tmp_giri+=1
            if risultato[1] == 0:
                turno += 1
            else:
                turno = 0
                colonna += 1
                if colonna > 3 : colonna = 1
        if saldo < puntata :
            # print(f"HAI PERSO TUTTO, round {tmp_giri}, saldo rimasto {saldo}€")
            tmp_giri = giri
            return "PERSO",tmp_giri,saldo
        if turno >= len(fibonacci):
            # print(f"HAI PERSO per fibonacci, round {tmp_giri}, saldo rimasto {saldo}€")
            turno=0
            return "PERSO",tmp_giri,saldo

    # print(f"alla fine di {giri} giri torni a casa con {saldo}€")
    return "VINTO",tmp_giri,saldo

if __name__ == "__main__":
    tot =100
    w = 0
    l = 0
    for i in range(tot):
        x = gioca(500,5,100)
        if x[0] == "PERSO": 
            l+=1
        else:
            w+=1
        # print(f"Hai {x[0]} giri torni a casa con {x[2]}€")
    print(f"W:{w}, L:{l}, tot:{tot}")
