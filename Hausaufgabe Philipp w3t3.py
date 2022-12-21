# Aufgabe 1
# Schreibt mir eine Geschichte (print). Nutzt die folgenden Variablen
# name1 = Peter Maier
# name2 = Stephanie Rückli
# fahrzeug = Fahrrad
# laenge_in_meter = 50
# geldbeutel_inhalt = 2000

import os
from time import sleep

os.system("cls")

name1 = "Peter Maier"
name2 = "Stephanie Rückli"
fahrzeug = "Fahrrad"
laenge_in_meter = 50
geldbeutel_inhalt = 2000

print(
    name1,
    "und",
    name2,
    "fuhren mit dem",
    fahrzeug,
    "in den Urlaub. Leider verloren sie bereits auf den ersten",
    laenge_in_meter,
    "Metern ihren Geldbeutel, welcher zu dem Zeitpunkt ihre gesamte Reisekasse in Höhe von",
    geldbeutel_inhalt,
    "Euro beinhaltete.",
)

# Aufgabe 2

# Erstelle ein Programm, welches die folgenden Informationen bei Kunden eines Reisebüros
# erfragt.
# Reiseziel
# Reisedauer
# Anreiseart
# Temperatur
# Essenspreferenz
# Kleidergröße für die Bademäntel
# Und gib die Informationen in einen Text aus.z.B.
# Sie möchten also nach Schweden reisen und 14 Tage dort im Hotel verweilen. Sie reisen mit
# dem Auto an und wünschen sich eine Temperatur von 25 Grad. Sie Essen gern Fisch und
# bräuchten einen Bademantel der Größe 38. Vielen Dank für ihre Bestellung

sleep(8)

reiseziel = input("Wohin soll es gehen? ")
reisedauer = input("Wie lange möchten sie reisen? ")
anreiseart = input("Womit möchten sie anreisen? ")
temperatur = input("Welche ungefähre Temperatur wünschen sie sich am Urlaubsort? ")
lieblingsessen = input("Über welches Essen würden sie sich freuen? ")
kleidergroesse = input("Welche Kleidergröße haben sie? ")

os.system("cls")

print(
    f"""Sie möchten also nach {reiseziel} reisen und {reisedauer} dort im Hotel verweilen. Sie reisen mit
dem {anreiseart} an und wünschen sich eine Temperatur von {temperatur}. Sie Essen gern {lieblingsessen} und
bräuchten einen Bademantel der Größe {kleidergroesse}. Vielen Dank für ihre Bestellung."""
)
