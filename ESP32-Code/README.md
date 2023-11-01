# ESP32 How to start Guid

 ## Firmware aufspielen
 - Thonny installieren [hier](https://thonny.org/)
 - ESP32 an PC anschließen
 - In Thonny "Run"->"Select interpreter"
       
    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/fe69f5f6-1801-44ac-aba3-85ee5202965d)

### Thonny options
- "MicroPython (ESP32)" Auswählen
      
  ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/f0019266-0c56-4a28-a169-756cbfef6d9c)

- richtigen COM Port auswählen (welcher ist der richtige? [hier](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/blob/42d86eff00d4ad49dd1e11dd36ada3a8d2ca3a8d/findingComPort.md))

    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/fad50f41-2ce6-48c6-8888-26386a93a186)

- "Install or update MicroPython"

    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/1a3f6be3-98ae-44cf-bb0c-289f55ded117)

### Install MicrtoPython (esptool)
- Com Port auswählen und Kontroller auswählen wie im Bild

  ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/f3427dad-2f69-4a4c-b670-c22812ea8407)

- "Install" klicken & Boot Button des ESP32 kurz drücken, danach "close"

    ![image](https://github.com/JJOmin/Projektgruppe-Smarter-Blumentopf/assets/104137706/9292c96b-0d6f-4ba6-8632-83c8f3f52903)

  ### Pyrhon auf ESP32 spielen und ausführen
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




  



