import os

os.system("cls")
vorname = input("Wie lautet dein Vorname?\n")
nachname = input("Wie lautet dein Nachname?\n")
iD = input("Bitte gib deine ID an.\n")

os.system("cls")
print("Datenbankeintrag erfolgt...\n")
print(
    f"""
      Vorname: {vorname.lower()}
      Nachname: {nachname.upper()}
      ID: {iD}
      """
)
