from time import sleep
import network

sta_if = network.WLAN(network.STA_IF)   # WiFi in station-modus zetten
sta_if.active(True)                     # WiFi aanzetten
sta_if.connect('<SSID>', '<password>')  # verbinden met WiFi

while not sta_if.isconnected():         # wachten op connectie
    print("Connecting...")
    sleep(0.5)
    
print("IP config: ", sta_if.ifconfig()) # IP-adres e.d. printen
