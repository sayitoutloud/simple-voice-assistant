# simple-voice-assistant

## Requirements
- Install LM Studio on your System (Windows) and activate the localhost API
- Raspberry Pi (4)
- Reverse Proxy Service: apache, nginx (I use xampp)

## Reverse Proxy Config
For xampp:
xampp\apache\conf\httpd.conf   
activate these two lines
```
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
```

xampp/apache/conf/extra/httpd-vhosts.conf   
add
```
<VirtualHost *:80>
    ServerName localhost
    DocumentRoot "C:/xampp/htdocs"

    ProxyRequests Off
    ProxyPreserveHost On

    <Proxy *>
        Require all granted
    </Proxy>

    ProxyPass /lmstudio-api/ http://localhost:1234/
    ProxyPassReverse /lmstudio-api/ http://localhost:1234/
</VirtualHost>
```

## Make python environment
```
sudo apt update
sudo apt install python3-venv
mkdir ~/meine_app
cd ~/meine_app
python3 -m venv venv
source venv/bin/activate
```

## Voice recognation & change it to text
```
pip install SpeechRecognition
pip install PyAudio
```

Google akzeptiert Audio nur in bestimmten Formaten (z. B. FLAC oder WAV)
Die speech_recognition-Bibliothek wandelt dein aufgenommenes Audio automatisch ins FLAC-Format um
Dafür wird das externe Tool flac verwendet (nicht in Python enthalten)
Ist es nicht vorhanden, bekommst du genau den Fehler, den du jetzt siehst
```
sudo apt update
sudo apt install flac
```


## TTS Part (make sure! you have already SpeechRecognition installed)
```
pip install gtts playsound pygame
sudo apt install python3-gi gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
```

