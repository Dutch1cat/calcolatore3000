while True:
    print("calcolatore 3000")
    print("1. avvia")
    print("2. esci")
    print("3. crediti")
    operazione = 0
    calcola_area = 0
    teorema_pitagora = 0
    scelta_iniziale = input("Risposta: ").strip().lower()
    if scelta_iniziale == "1":
        print("cosa vuoi fare?")
        print("1. un operazione")
        print("2. calcolare un area")
        print("3. teorema di pitagora")
        scelta1 = input("Risposta: ").strip().lower()
        if scelta1 == "1":
            operazione = 1
        if scelta1 == "2":
            calcola_area = 1
        if scelta1 == "3":
            teorema_pitagora = 1
    if scelta_iniziale == "2":
        break
    if scelta_iniziale == "3":
        print("creato da Luca Simonetti 3B anno 2024-25 scuola ungaretti")
    if operazione == 1:
        print("ok, cosa vuoi fare?")
        print("1. addizione")
        print("2. sottrazione")
        print("3. moltiplicazione")
        print("4. divisione")
        print("5. radice quadrata")
        print("6. potenza")
        scelta_operazione = input("Risposta: ").strip().lower()
        if scelta_operazione == "1":
            primo_termine_addizzione = float(input("primo numero: "))
            secondo_termine_addizzione = float(input("secondo numero: "))
            print(primo_termine_addizzione+secondo_termine_addizzione)
        if scelta_operazione == "2":
            primo_termine_sottrazione = float(input("primo numero:"))
            secondo_termine_sottrazione = float(input("secondo numero:"))
            print(primo_termine_sottrazione-secondo_termine_sottrazione)
        if scelta_operazione == "3":
            primo_termine_moltiplicazione = float(input("primo numero:"))
            secondo_termine_moltiplicazione = float(input("secondo numero:"))
            print(primo_termine_moltiplicazione*secondo_termine_moltiplicazione)
        if scelta_operazione == "4":
            primo_termine_divisione = float(input("primo numero:"))
            secondo_termine_divisione = float(input("secondo numero:"))
            print(primo_termine_divisione/secondo_termine_divisione)
        if scelta_operazione == "5":
            numero_radice_quadrata = float(input("numero:"))
            print(numero_radice_quadrata**(1/2))
        if scelta_operazione == "6":
            numero_potenza = float(input("numero:"))
            potenza = float(input("potenza:"))
            print(numero_potenza**potenza)
    if calcola_area == 1:
        print("di che figura vuoi calcolare l'area?")
        print("1. quadrato")
        print("2. rettangolo")
        print("3. triangolo")
        print("4. rombo")
        print("arriveranno altre figure con i prossimi update")
        area_iniziale = input("risposta:").strip().lower()
        if area_iniziale == "1":
            area_quadrato = float(input("lato del quadrato: "))
            print(area_quadrato*area_quadrato)
        if area_iniziale == "2":
            area_rettangolo_base = float(input("base: "))
            area_rettangolo_altezza = float(input("altezza: "))
            print(area_rettangolo_base*area_rettangolo_altezza)
        if area_iniziale == "3":
            area_triangolo_base = float(input("base: "))
            area_triangolo_altezza = float(input("altezza: "))
            print(area_triangolo_base*area_triangolo_altezza/2)
        if area_iniziale == "4":
            print("vuoi calcolare usando le diagonali o lato e altezza(come se fosse un parallelogramma)?")
            print("1. diagonali")
            print("2. base e altezza")
            area_rombo = input("risposta:").strip().lower()
            if area_rombo ==  "1":
                area_rombo_diagonale1 = float(input("diagonale numero 1: "))
                area_rombo_diagonale2 = float(input("diagonale numero 2: "))
                print(area_rombo_diagonale1*area_rombo_diagonale2/2)
            if area_rombo == "2":
                area_rombo_base = float(input("lato: "))
                area_rombo_altezza = float(input("altezza: "))
                print(area_rombo_base*area_rombo_altezza)
    if teorema_pitagora == 1:
        print("cosa hai?")
        print("1. un cateto e ipotenusa")
        print("2. 2 cateti")
        scelta_pitagora = input("risposta:").strip().lower()
        if scelta_pitagora == "1":
            ipotenusa = float(input("ipotenusa: "))
            cateto = float(input("cateto: "))
            print((ipotenusa**2-cateto**2)**(1/2))
        if scelta_pitagora == "2":
            cateto1 = float(input("cateto 1: "))
            cateto2 = float(input("cateto 2: "))
            print((cateto1**2+cateto2**2)**(1/2))