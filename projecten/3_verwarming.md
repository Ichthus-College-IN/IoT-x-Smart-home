# Verwarming

## Omschrijving
*Niets zo fijn als een goede temperatuur in huis! Je werkt met twee
  temperatuursensoren, verwarming en twee ventilatoren om het huis
  een aangename temperatuur te geven. Zo kun je zelfs het huis
  voorverwarmen als je nat thuiskomt, of extra energie besparen door
  de verwarming uit te schakelen als er niemand thuis is. Win-win!*

## Informatie
Je gebruikt twee temperatuursensoren: de BMP280 (https://www.tinytronics.nl/shop/nl/sensoren/lucht/druk/bmp280-digitale-barometer-druk-sensor-module). Hiermee kun je onder en boven in het huis de temperatuur meten. Daarnaast heb je twee ventilatoren tot je beschikking: https://www.tinytronics.nl/shop/nl/mechanica-en-actuatoren/ventilatoren/kleine-ventilator-voor-raspberry-pi-behuizing. Verder nog een verwarmingselement: https://www.amazon.nl/dp/B088ZVPBNF/ref=pe_28126711_487102941_TE_SCE_dp_1. Beetje sketchy, maar hopelijk doet 'ie wat 'ie moet doen, namelijk verwarmen. De verwarming bevindt zich alleen op de benedenverdieping; luchtkoeling aan de ene kant onder in het huis en aan de andere kant boven. De verwarming verbruikt volgens het boekje ongeveer 8W, wat (pun intened) veel teveel is voor de ESP32. Daarom is deze rechtstreeks aangesloten op de power supply, maar met behulp van een transistor (https://www.tinytronics.nl/shop/nl/componenten/transistoren/npn-transistor-bc547 (**TODO:** andere transistor! Max 0.1A)). Ook de ventilator kun je beter met een transistor bedienen.

## Opdracht
Maak een automatische thermostaat, die de temperatuur via MQTT weergeeft voor beide verdiepingen, en die voor beide verdiepingen als input een temperatuur accepteert. Vervolgens ga je het huis opwarmen of juist afkoelen, of voor beide verdiepingen verschillend.

Als dat gelukt is, ga je nadenken over een geautomatiseerd systeem: 's nachts hoeft de verwarming eigenlijk niet aan te staan, tot iets voordat je wakker wordt. Of als er niemand thuis is (dat kan via Home Assistant herkend worden), schakelt het systeem weer uit.