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

Google only accepts audio in certain formats (e.g., FLAC or WAV). The speech_recognition library automatically 
converts your recorded audio to the FLAC format. For this, it uses the external tool flac (not included with Python). 
If it's not available, you'll get exactly the error you're seeing now.
```
sudo apt update
sudo apt install flac
```


## TTS Part (make sure! you have already SpeechRecognition installed)
```
pip install gtts playsound pygame
sudo apt install python3-gi gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
```

