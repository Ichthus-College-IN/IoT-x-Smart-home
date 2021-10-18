# Entertainment (1)

## Omschrijving
*Iedereen geniet van een stukje muziek op zijn tijd. Het mag dan
  geen Spotify worden, maar je gaat je eigen muziekspeler bouwen
  met behulp van vooropgeslagen mp3'tjes. Een speaker is aanwezig
  in huis.*

## Informatie
In de woonkamer is een speaker ingebouwd: https://www.tinytronics.nl/shop/nl/audio/speakers/speakers/kleine-speaker-4%CF%89-3w. Hierop kun je zelf je eigen muziekjes afspelen. Maar: mp3'tjes zijn veel te zwaar voor de magere 4 MB geheugen op de ESP32, die ook niet echt makkelijk te gebruiken is. Daarom is er ook een externe SD-kaart met SD-kaartlezer: https://www.tinytronics.nl/shop/nl/data-opslag/modules/microsd-kaart-adapter-module-3.3v-5v-met-level-shifter. Hierop kun je je liedjes opslaan, om ze vervolgens af te spelen op de speaker.

## Opdracht
Bouw een entertainmentsysteem waarbij liedjes afgespeeld kunnen worden. Hierbij kan de gebruiker het liefst ook selecteren welk nummer er afgespeeld wordt. Dat kan op basis van nummers, maar helemaal mooi als zelfs de titels geselecteerd kunnen worden. Het liefst kun je zelfs tijdens een nummer skippen naar het volgende nummer, als je het zat bent.

Zodra dit gelukt is, kun je zelfs kijken naar synchroniseren met andere events. Als er bijvoorbeeld iemand thuis komt (dat kan gedetecteerd worden met Home Assistant), gaat er een nummer afspelen. Of je spreekt met een ander groepje af dat er een signaal verzonden wordt naar jouw ESP waarbij je dan een nummertje speelt.