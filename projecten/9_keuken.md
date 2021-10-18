# Keuken

## Omschrijving
*Zelfs in de keuken kun je de idee* smart home *toepassen. Bij
  dit project simuleer je bijvoorbeeld een keramische kookplaat, maar
  de kookkunsten van jou of je partner laten nog wel eens te wensen
  over. Een CO- en rookmelder zijn dus geïnstalleerd om ervoor
  te zorgen dat je op tijd weet dat het tijd is om Domino's te halen.
  Je laat namelijk op een buzzer een alarm afgaan als de gemeten 
  waarden te hoog worden.*

## Informatie
Met behulp van een LED die aangesloten is op PWM kun je een keramische kookplaat simuleren. Een echt verwarmingselement op dit niveau is helaas niet echt haalbaar. Wel zitten er in de keuken twee luchtkwaliteitssensoren: een rookmelder (https://www.tinytronics.nl/shop/nl/sensoren/lucht/gas/mq-2-gas-sensor-module) en een CO-melder (https://www.tinytronics.nl/shop/nl/sensoren/lucht/gas/mq-7-gas-sensor-module). Let op dat de MQ-2 veel meer meet dan alleen rook: je zult hier dus mee aan de slag moeten om een betrouwbare waarde te vinden. Daarnaast beschik je over een standaard buzzer (https://www.tinytronics.nl/shop/nl/audio/speakers/buzzers/actieve-buzzer-5v) om een alarm af te laten gaan in geval van nood.

## Opdracht
Bouw een 'kookplaat' die op verschillende standen aangezet kan worden. Bouw daarnaast een systeem dat luchtkwaliteit meet voor rook en koolstofmonoxide. Als de waarden te hoog worden (welke drempelwaarden zijn dat?) gaat een alarm af. Monitor via MQTT de gemeten hoeveelheiden en zorg dat er in Home Assistant voor beide sensors grafieken gemaakt worden.

Als dit gelukt is, kun je via Home Assistant misschien de drempelwaarden voor het alarm aanpasbaar maken, of voeg je extra lampjes toe aan de kookplaat.