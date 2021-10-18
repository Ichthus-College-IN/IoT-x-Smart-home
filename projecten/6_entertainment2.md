# Entertainment (2)

## Omschrijving
*In voor een uitdaging? In het huis is een 8 bij 8 LED matrix
  aanwezig die als fotomuur functioneert. Hier maak je een
  eigen webserver waar je fotootjes kunt uploaden die in twee
  kleuren (of misschien zelfs RGB) weergegeven kunnen worden op
  deze matrix. Hierbij komt meer om het hoekje kijken dan alleen
  programmeren in Python!*

## Informatie
Een 8×8 Neopixel matrix is een van de leukste componenten die er is (https://www.adafruit.com/product/1487). Om er wat nuttigs op weer te geven is echter een ander verhaal: een van de moeilijkere dingen. Voor de matrix-varianten zijn er op internet niet zoveel voorbeelden aanwezig in MicroPython. Niet getest is hier een optie: https://github.com/mcauser/micropython-max7219. Mocht dat niet werken is hier een optie voor een 16×16 matrix library: https://github.com/micropython-Chinese-Community/mpy-lib/tree/master/neopixel. Misschien weet je het aan te passen naar 8×8. Of we chainen er vier aan elkaar en maken er alsnog 16 bij 16 van.

## Opdracht
Bouw een service waarbij foto's kunnen worden weergegeven op deze matrix. Let op dat zo'n 'foto' maximaal 8 bij 8 pixels is, omdat de rest er dan weer afvalt (tenzij we er een 16 bij 16 van maken). Begin met een normale bitmap van 8 bij 8 in één kleur, en breid vervolgens uit naar RGB en misschien andere bestandsformaten. Om toch de verbindng met Home Assistant te benutten zorg je voor een aan/uit-schakelaar over MQTT.

Zodra dat gelukt is, lanceer je een webservice waarop foto's van het goede formaat geüpload kunnen worden, waarna ze weergegeven worden op de matrix.