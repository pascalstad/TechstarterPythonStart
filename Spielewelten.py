import os
from time import sleep

os.system("cls")
welten = [1, 2, 3]
welt = welten[0]
beenden = 0
gegenstandInWelt = 1
print("Willkommen in Welt ", welt, "\n")
while beenden == 0:
    while gegenstandInWelt == welt:
        os.system("cls")
        print("Willkommen auf Welt", welt)
        aktion = int(
            input(
                "Sie können \n 0 einen Gegenstand aufnehmen\n 1 sich nach Welt 1 bewegen\n 2 sich nach Welt 2 bewegen\n 3 sich nach Welt 3 bewegen\n 4 aktuelle Welt anzeigen\n 5 Spiel beenden\n"
            )
        )
        if aktion == 0:
            print("Sie haben einen Gegenstand aufgenommen\n")
            gegenstandInWelt = 4
            sleep(2)
        elif aktion == 1:
            if welt == 1:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[0]
        elif aktion == 2:
            if welt == 2:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[1]
        elif aktion == 3:
            if welt == 3:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[2]
        elif aktion == 4:
            os.system("cls")
            print("Sie befinden sich aktuell in Welt", welt, "\n")
            sleep(2)
        elif aktion == 5:
            print("Vielen Dank fürs Spielen\n")
            beenden = 1
            break
    while gegenstandInWelt == 4:
        os.system("cls")
        print("Willkommen auf Welt", welt)

        aktion = int(
            input(
                "Sie können \n 0 einen Gegenstand ablegen\n 1 sich nach Welt 1 bewegen\n 2 sich nach Welt 2 bewegen\n 3 sich nach Welt 3 bewegen\n 4 aktuelle Welt anzeigen\n 5 Spiel beenden\n"
            )
        )
        if aktion == 0:
            print("Sie haben einen Gegenstand abgelegt\n")
            sleep(2)
            gegenstandInWelt = welt
        elif aktion == 1:
            if welt == 1:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[0]
        elif aktion == 2:
            if welt == 2:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[1]
        elif aktion == 3:
            if welt == 3:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[2]
        elif aktion == 4:
            os.system("cls")
            print("Sie befinden sich aktuell in Welt", welt, "\n")
            sleep(2)
        elif aktion == 5:
            print("Vielen Dank fürs Spielen\n")
            beenden = 1
            break
    while gegenstandInWelt != 4 and gegenstandInWelt != welt:
        os.system("cls")
        print("Willkommen auf Welt", welt)
        aktion = int(
            input(
                "Sie können \n 1 sich nach Welt 1 bewegen\n 2 sich nach Welt 2 bewegen\n 3 sich nach Welt 3 bewegen\n 4 aktuelle Welt anzeigen\n 5 Spiel beenden\n"
            )
        )
        if aktion == 1:
            if welt == 1:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[0]
        elif aktion == 2:
            if welt == 2:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[1]
        elif aktion == 3:
            if welt == 3:
                print("Sie befinden sich bereits hier.\n")
                sleep(2)
            else:
                welt = welten[2]
        elif aktion == 4:
            os.system("cls")
            print("Sie befinden sich aktuell in Welt", welt, "\n")
            sleep(2)
        elif aktion == 5:
            print("Vielen Dank fürs Spielen\n")
            beenden = 1
            break
