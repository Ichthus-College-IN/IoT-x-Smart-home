# Moestuin

## Omschrijving
*Niet alleen het huis zelf is smart, ook buiten het huis valt
  er genoeg te automatiseren en te bedienen. Daarnaast voorzie
  je de bewoners ook nog eens van een beetje groenvoer: je
  zorgt ervoor dat jouw echte planten voorzien worden van genoeg
  water door een vochtsensor en pomp te gebruiken. Daarnaast houd
  je het waterpeil in de 'regenton' in de gaten om te voorkomen
  dat het droogvalt. Pluspunt als je serieus iets weet te verbouwen! :)*

## Informatie
Bij het huis zit ook een moestuin. Hierbij zit een pompsysteem met de volgende pomp: https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/motoren/pompen/onderwaterpomp-horizontaal-3-6v. Daarnaast zijn er een bodemvocht- en waterpeilsensor aanwezig: https://www.eijlander.nl/arduino-compatibele-bodemvochtsensor-waterpeilsensor.html. Beide geven een analoge waarde als output. Het water zit in een regenton oftewel waterfles aan de zijkant van het huis.

## Opdracht
Bouw een watervoorziening voor je plantjes in de moestuin. Als het bodemvochtgehalte te laag wordt pomp je er extra water bij, en als het waterpeilgehalte in de regenton te laag wordt, moet er op een of andere manier gealarmeerd worden dat er bijgevuld moet worden. Hoe dat precies gedaan wordt is aan jullie. Via MQTT worden de waardes van het bodemvocht en de regenton gerapporteerd, en kan er ook ingesteld worden bij welke waarde het alarm afgaat voor de regenton, en wanneer de moestuin weer gewaterd wordt.

Zodra dat redelijk gelukt is, plant je zelfs wat in de moestuin en probeer je echt wat te verbouwen!