# Verduistering

## Omschrijving
*Net zoals verlichting is verduistering ook een goed concept om te
  automatiseren. Je gaat aan de slag met 4 motoren om gordijnen
  te openen en sluiten op basis van zonsopkomst en -ondergang.
  Dan kun je zelfs de gordijnen open doen als je weg was en je ouders
  dat niet mogen weten..*

## Informatie
Je hebt de beschikking over 4 servo's van het type SG90; om exact te zijn deze: https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/motoren/servomotoren/sg90-mini-servo. Een servo is een motor die maximaal 360 graden kan draaien. Hoe je een servo bedient kun je op internet vinden (let op dat je zoekt op een MicroPython variant, niet op een C++ variant). Een voorbeeld van een library en script zijn hier te vinden: https://github.com/pvanallen/esp32-getstarted/blob/master/examples/servo.py en https://github.com/pvanallen/esp32-getstarted/blob/master/examples/servo_move.py respectievelijk. Deze zijn niet getest en misschien helemaal niet de beste, maar het is een startpunt. 

Tip: lees eerst wat rond over servo's, voordat je er zomaar mee begint.

## Opdracht
Bouw je project zodanig, dat er per gordijn een open/dicht schakelaar gebruikt kan worden (over MQTT uiteraard). Daarnaast kan er met behulp van een slider voor elk gordijn een tussenstand gebruikt worden, als bijvoorbeeld de zon net om het hoekje van het raam komt. Want dan hoeft het gordijn niet opeens in zijn geheel dicht.

Zodra dat gelukt is zoek je via internet op hoe je de zonsop- en ondergang kunt ophalen / berekenen, en zorg je ervoor dat de gordijnen automatisch open en dicht gaan als dat nodig is. Ze moeten dan weer niet open gaan als ze al dicht zijn vóór de zonsondergang.