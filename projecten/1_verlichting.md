# Verlichting

## Omschrijving
*Je gaat aan de slag om 4 (RGB) LEDs door het huis aan te sturen: voor elke kamer één. Op basis van zonsopkomst en -ondergang gaan ze automatisch aan en uit en de helderheid en/of kleur kunnen geregeld worden. Zo hoef je nooit meer je bed uit om de lichtknop uit te zetten.*

## Informatie
Je hebt de beschikking over 4 stuks RGB LED. Om precies te zijn deze: https://www.tinytronics.nl/shop/nl/componenten/led's/led's/rgb-led-5mm-diffuus-common-cathode.
De werking hiervan is erg eenvoudig: één pin is de Ground, de andere drie zijn de drie kleuren rood, groen en blauw. Hoe hoger de waarde op een pin, hoe meer die kleur voorkomt.

Een voorbeeld voor de ESP32 op MicroPython kan hier gevonden worden: https://github.com/danielwohlgemuth/blinking-led-micropython-esp32.

## Opdracht
Bouw je project zodanig, dat er per lamp een aan/uit-knop gebruikt kan worden (over MQTT uiteraard), en daarnaast per lamp drie sliders waarmee de waarden voor RGB bepaald kunnen worden. Je zult dus een flink aantal *topics* moeten gebruiken, al kun je ze misschien combineren.

Zodra dat gelukt is zoek je via internet op hoe je de zonsop- en ondergang kunt ophalen / berekenen, en zorg je ervoor dat de lampen automatisch aangaan en uitschakelen als dat nodig is. Ze moeten dan weer niet uitschakelen als ze al aanstaan vóór de zonsondergang.

Daarnaast is het nog een mogelijkheid om *helderheid* toe te voegen. Zo hoef je niet alle drie de sliders voor RGB te dimmen om de lamp in zijn geheel donkerder te maken.