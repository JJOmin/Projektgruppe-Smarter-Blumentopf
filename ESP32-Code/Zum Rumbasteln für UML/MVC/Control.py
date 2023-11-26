#Control
from Server import Server
ssid = 'Flat mars society 5G death laser'
password = '5G power'
remote_url = 'https://www.tilly.cloud/Blumentopf/Database/daten.json'  # falls fehler auftrete auf "https://cloudleo.duckdns.org/Blumentopf/Database/daten.json" setzen
upload_url = 'https://blumentopfupload.tilly.cloud/Blumentopf/upload_data'  # falls fehler auftreten auf "http://31.19.90.130:5000/Blumentopf/upload_data" setzen
username = b'Blumentopf'
password_b = b'Blumentopf_123'

Server = Server(ssid, password, remote_url, upload_url, username, password_b)
Server.connectWifi()
print(Server.getRemote())
print(Server.setTestDataToServer())
print(Server.getRemote())