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

## Request Script (Python)
```
import requests

url = "http://10.0.0.45/lmstudio-api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer lm-studio"
}

data = {
    "model": "llama3:8b",
    "messages": [{"role": "user", "content": "Hallo!"}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

```
