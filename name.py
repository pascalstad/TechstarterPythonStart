import os
from time import sleep

os.system("cls")

vorname = input("Wie lautet dein Vorname? ")
nachname = input("Wie lautet dein Nachname? ")
alter = input("Wie alt bist du? ")
beruf = input("Was ist dein Beruf? ")
groesse = input("Wie groß bist du? ")
schuhGroese = input("Welche Schuhgröße hast du? ")
gehalt = input("Wie hoch ist dein derzeitiges Gehalt? ")

os.system("cls")

sleep(2)

print(
    f"""
      Peronalformular
      
      Name: {vorname} {nachname}
      Alter: {alter}
      Beruf: {beruf}
      Größe: {groesse}
      Schuhgröße: {schuhGroese}
      Gehalt: {gehalt}
      
      """
)
