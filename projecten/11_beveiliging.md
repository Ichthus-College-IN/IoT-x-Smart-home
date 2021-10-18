# Beveiliging

## Omschrijving
*Staat je vriend voor de deur maar ben je te druk bezig met
  gam.. ehh, huiswerk? Doe de deur automatisch open. Daarnaast
  bevindt zich in het huis een kluis die alleen met een pas
  geopend kan worden. Die pas kun je echter via het internet
  aanmelden. Je bouwt met twee servo's een automatisch systeem
  dat onder andere reageert op een RFID-pas.*

## Informatie
Met behulp van RFID (dat is eigenlijk NFC) kun je authorizatie toepassen. Je gebruikt een RFID-scanner en passen (https://www.tinytronics.nl/shop/nl/communicatie-en-signalen/draadloos/rfid/rfid-kit-mfrc522-s50-mifare-met-kaart-en-key-tag) kun je reguleren wie de deur open kan doen en wie niet. In combinatie met twee servo's (https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/motoren/servomotoren/sg90-mini-servo) bescherm je de voordeur en kluis tegen ongewenste personen.

## Opdracht
Bouw een systeem waarbij je met behulp van een RFID-token het slot op de toegangsdeur en/of kluisdeur kunt openen en sluiten. Via MQTT geef je weer of de deuren open en/of gesloten zijn, en kun je ze ook openen of sluiten d.m.v. een knop voor elke deur. Daarbij is er een kaart die alleen de voordeur kan openen, en een kaart die de voordeur én de kluis kan ontgrendelen.

Mocht dit gelukt zijn, breid je je systeem uit met een aanmeldingsmogelijkheid voor nieuwe passen. Zo kun je toevoegen welke passen welke functionaliteiten hebben. Let op: dit moet wel over internet kunnen gebeuren. Hoe precies, is aan jullie.