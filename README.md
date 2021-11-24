# IoT-x-Smart-home
'Internet of Things gecombineerd met Smart home op de ESP32' module - Ichthus College Veenendaal

Deze repository bevat de benodigde informatie om met de 
ESP32 aan de slag te gaan, plus per opdracht de
bijbehorende informatie wat betreft de opdracht en de
sensoren en actuatoren.

Voor een vrij beknopt maar volledig overzicht van de
functionaliteit van MicroPython op de ESP32 kan de website
https://docs.micropython.org/en/latest/esp32/quickref.html#
geraadpleegd worden.

## Instructies
- Maak in je eigen repository een **map** met de naam IoT-Smart-home.
- Sla daarin je **.py** bestanden op.
- Eén persoon uit het groepje wordt aangewezen om de goede bestanden te **uploaden** op GitHub.
- Houd bij het uploaden in GitHub een goed **logboek** bij: deze wordt aan het einde van de periode **beoordeeld**.
- De groepsopdracht is in zijn geheel het **eindcijfer**, maar de reflectie wordt **persoonlijk** beoordeeld. Je cijfer kan dus net wat verschillen.

## Planning
- Week 1: introductie Internet of Things en Smart home, startopdracht
- Week 2: experimenteren met MicroPython en de ESP32, product bouwen
- Week 3-6: product bouwen
- Kerstvakantie
- Week 7: product bouwen en opleveren

## Pinout schema
https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/ESP32-DOIT-DEVKIT-V1-Board-Pinout-30-GPIOs-Copy.png?resize=966%2C574&ssl=1

## Teacher's note
```bash
pip install esptool
esptool --chip esp32 --port COM4 erase_flash
esptool --chip esp32 --port COM4 --baud 115200 write_flash -z 0x1000 Downloads\esp32-20210902-v1.17.bin
```
