# If Aufgabe:

# Erstelle ein Programm, das Temperaturwerte einliest und anhand von diesen Hinweise zum Wetter gibt. Wertebereiche: (unter 0°, 0° bis 10°, 11° bis 20°, 20° bis 30°, über 30°

# Eingabe 40 Grad
# Ausgabe Programm:

# Es ist heiß. Nicht zu viel körperlich tätig sein. Viel trinken.

# Eingabe -10 Grad
# Ausgabe Programm:

# Es ist sehr kalt. Bitte zieh dir warme Kleidung an.

# while Aufgabe

# Lass das oben erstellte Programm in einer while Schleife laufen. Der Benutzer soll die Temperatur solange ändern können, bis wir das Programm mit der Eingabe von q beenden.

x = ""
while x != "q":
    x = input("Bitte gib die aktuelle Temperatur an.\n")
    if x == "q":
        break
    if int(x) < 0:
        print("Es ist sehr kalt. Bitte zieh dir warme Kleidung an.\n")
    elif int(x) > -1 and int(x) < 11:
        print("frisch heute. brrr")
    elif int(x) > 10 and int(x) < 21:
        print("nett heute.")
    elif int(x) > 20 and int(x) < 30:
        print("super Wetter...")
    elif int(x) > 29:
        print("Es ist heiß. Nicht zu viel körperlich tätig sein. Viel trinken.")
    else:
        print("Falsche Eingabe")
