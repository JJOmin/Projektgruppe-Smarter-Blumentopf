# ESP32 How to start Guid

 ## 1. ESP32 mit (Win/Mac) verbinden
 - Thonny IDE installieren [hier](https://thonny.org/)
 - Silicon Labs Treiber installieren [hier](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads)

   ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/b1af9ed0-bb50-43a1-85e9-ba0140373011)
 - Rechner neustarten!!!
 - Überprüfen ob Rechner ESP32 erkennt
   - Windows:
     - "[Win]()" + "[r]()" drücken, "[cmd]()" eintippen und "[OK]()"
     - Dann "[mode]()" eingeben und auf die ausgabe warten

       ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/f541a113-cfec-4f25-9071-4551b5f7e185)
     - Jetzt ESP32 per USB Kabel mit Rechner verbinden und noch einmal "[mode]()" 
     - Darauf achten welcher COM Port Neu ist (wie im Beispielbild)
      
       ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/c32a8f13-f5c1-4815-816f-7b3c1ea1dca4)
       
   - MacOS:
     - ESP32 per USB Kabel mit Rechner verbinden
     - Thonny IDE Öffnen
     - Weiter zu 2. Firmware aufspielen/ ESP32 Flashen
    


 ## 2. Firmware aufspielen/ ESP32 Flashen
 ### 2.1 Thonny Options
 - In Thonny "Run"->"Select interpreter"
       
    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/fe69f5f6-1801-44ac-aba3-85ee5202965d)

- "MicroPython (ESP32)" Auswählen
      
  ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/f0019266-0c56-4a28-a169-756cbfef6d9c)

### 2.2 Richtigen COM Port auswählen/ 
 -

    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/fad50f41-2ce6-48c6-8888-26386a93a186)

- "Install or update MicroPython"

    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/1a3f6be3-98ae-44cf-bb0c-289f55ded117)

### 2.2 Install MicrtoPython (esptool)
- Com Port auswählen und Kontroller auswählen wie im Bild

  ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/f3427dad-2f69-4a4c-b670-c22812ea8407)

- "Install" klicken & Boot Button des ESP32 kurz drücken, danach "close"

    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/9292c96b-0d6f-4ba6-8632-83c8f3f52903)

  ### 2.3 Pyrhon auf ESP32 spielen und ausführen
- Eine main.py erstellen "File"->"New"
- MicroPython Interpreter für ESP32 Auswählen

  ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/adc4286f-d8b3-408b-98e8-20b6b9cab35d)

- Beispielcode einfügen:
  
        print("Scanning for WiFi networks, please wait...")
        print("")
  
        import network
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
  
        authmodes = ['Open', 'WEP', 'WPA-PSK' 'WPA2-PSK4', 'WPA/WPA2-PSK']
        for (ssid, bssid, channel, RSSI, authmode, hidden) in sta_if.scan():
          print("* {:s}".format(ssid))
          print("   - Auth: {} {}".format(authmodes[authmode], '(hidden)' if hidden else ''))
          print("   - Channel: {}".format(channel))
          print("   - RSSI: {}".format(RSSI))
          print("   - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
          print()

  - Ausführen mit "Run" -> "Run current Interpreter" oder "F5" auf dem ESP32 ausführen
    
      ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/e334fc79-70bd-43b9-a2af-98ca7c530a60)




  



