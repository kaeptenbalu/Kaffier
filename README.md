# Kaffier
Kaffier ist eine Flask Applikation für den entfernten Zugriff auf die
Kaffeemaschine [model xyz] und die Verwaltung seines Biervorrates.

## Installation
Kaffier befindet sich noch in der Entwicklung und ist daher noch nicht paketiert.

## Entwicklungsumgebung
Für die Entwicklungsumgebung wird git, python und python-virtualenv benötigt.

Debian
```
apt install git python-virtualenv
```

OpenSUSE
```
zypper install git python-virtualenv
```

### Python Virtualenv
```
git clone https://github.com/kaeptenbalu/Kaffier
cd Kaffier
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Python Flask
Für die Entwicklung muss die Umgebungsvariable FLASK_CONFIG auf den Wert
"development" gesetzt werden.

```
FLASK_CONFIG=development python manage.py db init
FLASK_CONFIG=development python manage.py db migrate
FLASK_CONFIG=development python manage.py db upgrade
FLASK_CONFIG=development python manage.py runserver
```
Die Flask App lauscht nun auf Port 5000 des localhosts.

### Datenbank
Für die Entwicklung wird eine sqlite3 Datenbank mit dem Namen "DevData.db"
angelegt.
