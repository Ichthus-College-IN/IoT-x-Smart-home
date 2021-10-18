# Oprijlaan

## Omschrijving
*Een hek voor je huis is soms geen overbodige luxe. Maar
  het liefst gaat dit wel automatisch open als jij aan komt
  rijden, of als je je vrienden aan ziet komen. En in het donker
  komt verlichting dan ook wel goed van pas. Je bouwt met een
  reed switch, servo, lichtsensor en lampjes een mooie oprijlaan.*

## Informatie
*Presence-detection* kan op een interessante manier door het gebruik van een reed-switch (https://www.tinytronics.nl/shop/nl/schakelaars/magneetschakelaars/reed-relais-2*14mm). In nabijheid van een magneet maken de ijzertjes contact en gaat er een stroompje lopen. Met behulp van een magneet in een auto kun je zo het contact activeren. Met een servo (https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/motoren/servomotoren/sg90-mini-servo) kun je vervolgens het hek openen. Om de oprijlaan te verlichten is er een lichtsensor (https://www.tinytronics.nl/shop/nl/sensoren/optisch/licht-en-kleur/gl5537-ldr-lichtgevoelige-weerstand of ander GL55xx type) en (voorlopig) een serie gewone LEDs.

## Opdracht
Bouw een systeem waarmee in het geval van aanwezigheid van een auto (magneet) de hekken opengaan en in het geval van een donker tijdstip de verlichting automatisch aangaat. Daarnaast moet het mogelijk zijn om via MQTT hetzelfde uit te voeren, of de verlichting los aan te zetten om de tuin op te lichten, ook als er niemand aankomt.

Mocht dat gelukt zijn, kun je bijvoorbeeld een mooi patroon op de lampjes zetten met behulp van PWM, of maken we er misschien RGB lampjes van om er helemaal wat moois van te maken.