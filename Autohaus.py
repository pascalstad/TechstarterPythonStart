parkplatz1belegt = True
parkplatz2belegt = True
parkplatz3belegt = True
parkplatz4belegt = True
parkplatz5belegt = True
parkplatz6belegt = True
done = False

while done == False:
    einOderAus = int(
        input(
            "Möchten Sie Ein- oder Ausparken? Geben Sie bitte die 1 für Einparken oder 2 für Ausparken ein.\n"
        )
    )
    while einOderAus == 1:
        autoMarke = int(
            input(
                "Bitte wählen SIe ihre Automarke aus\n 1 für Porsche\n 2 für Audi\n 3 für Peugeot\n 4 für VW\n 5 für BMW\n 6 für Ford"
            )
        )
        if autoMarke == 1:
            if parkplatz1belegt == False:
                print("Ihr Porsche wurde auf Parkplatz 1 abgeparkt.")
                parkplatz1belegt = True
                done = True
            else:
                print("Leider sind alle Parkflächen belegt.")
                done = True
        elif autoMarke == 2:
            if parkplatz2belegt == False:
                print("Ihr Audi wurde auf Parkplatz 2 abgeparkt.")
                parkplatz2belegt = True
                done = True
            else:
                print("Leider sind alle Parkflächen belegt.")
                done = True
        elif autoMarke == 3:
            if parkplatz3belegt == False:
                print("Ihr Peugeot wurde auf Parkplatz 3 abgeparkt.")
                parkplatz3belegt = True
                done = True
            else:
                print("Leider sind alle Parkflächen belegt.")
                done = True
        elif autoMarke == 4:
            if parkplatz4belegt == False:
                print("Ihr VW wurde auf Parkplatz 4 abgeparkt.")
                parkplatz4belegt = True
                done = True
            else:
                print("Leider sind alle Parkflächen belegt.")
                done = True
        elif autoMarke == 5:
            if parkplatz5belegt == False:
                print("Ihr BMW1 wurde auf Parkplatz 1 abgeparkt.")
                parkplatz5belegt = True
                done = True
            else:
                print("Leider sind alle Parkflächen belegt.")
                done = True
        elif autoMarke == 6:
            if parkplatz6belegt == False:
                print("Ihr Ford wurde auf Parkplatz 1 abgeparkt.")
                parkplatz6belegt = True
                done = True
            else:
                print("Leider sind alle Parkflächen belegt.")
                done = True

    while einOderAus == 2:
        parkplatzNummer = int(input("Bitte geben Sie ihre Parkplatznummer ein.\n"))
        if parkplatzNummer == 1:
            print("Vielen dank. Ihr Auto der Marke Porsche wird ausgeparkt.\n")
            parkplatz1belegt = False
            einOderAus = 0
            done = True
        elif parkplatzNummer == 2:
            print("Vielen dank. Ihr Auto der Marke Audi wird ausgeparkt.\n")
            parkplatz2belegt = False
            einOderAus = 0
            done = True
        elif parkplatzNummer == 3:
            print("Vielen dank. Ihr Auto der Marke Peugeot wird ausgeparkt.\n")
            parkplatz3belegt = False
            einOderAus = 0
            done = True
        elif parkplatzNummer == 4:
            print("Vielen dank. Ihr Auto der Marke VW wird ausgeparkt.\n")
            parkplatz4belegt = False
            einOderAus = 0
            done = True
        elif parkplatzNummer == 5:
            print("Vielen dank. Ihr Auto der Marke BMW wird ausgeparkt.\n")
            parkplatz5belegt = False
            einOderAus = 0
            done = True
        elif parkplatzNummer == 6:
            print("Vielen dank. Ihr Auto der Marke Ford wird ausgeparkt.\n")
            parkplatz6belegt = False
            einOderAus = 0
            done = True
        else:
            print("Bitte geben Sie eine gültige Parkplatznummer ein.\n")
