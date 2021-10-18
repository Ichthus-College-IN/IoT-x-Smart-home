# Badkamer

## Omschrijving
*De was aanzetten terwijl je voorlopig nog niet thuiskomt is niet
  het beste idee. Of men weet de instellingen niet zo goed, dus
  moet jij de wasmachine toch maar weer aanzetten. Je bouwt een
  namaak-wasmachine met een motortje, en daarnaast een werkende 
  douche (hopelijk) met een pomp. Zo kun je op een extra koude dag 
  direct onder het warme water springen.*

## Informatie
Met behulp van een stepper motor (waarschijnlijk https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/motoren/dc-motoren/kleine-dc-motor-3-6v) doen we een wasmachine na. Werkelijk water erin is niet het beste idee, maar het lijkt erop. Daarnaast is er een douche die circulair water rondpompt met behulp van een waterpomp (https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/motoren/pompen/onderwaterpomp-verticaal-3-6v). 

## Opdracht
Maak een werkende wasmachine en douche. Hier gaat het voornamelijk om een automatisch programma voor de wasmachine, en het aan/uit zetten via MQTT. Ook de douche is aan en uit te zetten met behulp van zo'n schakelaar. Let hierbij ook op de manier dat je programma draait: je moet ook de douche kunnen bedienen terwijl de wasmachine aanstaat. Dat is misschien moeilijker dan het klinkt.

Zodra dit werkt kun je ook verschillende programma's maken voor de wasmachine. Deze zijn te selecteren via Home Assistant.