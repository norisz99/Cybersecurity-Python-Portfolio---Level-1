# 🌍 IP Geolocation Tracker (CLI Tool)

## 📌 Áttekintés (Overview)
Ez a Python alapú eszköz lehetővé teszi IP címek és weboldalak fizikai helyzetének (Geolocation) meghatározását. A program egy nyilvános REST API-t (`ip-api.com`) használ az adatok lekéréséhez, és automatikusan kezeli a DNS névfeloldást is.

## 🛠️ Funkciók
* **📡 IP & Domain Támogatás:** Nemcsak IP címeket (`8.8.8.8`), hanem weboldalakat (`google.com`) is elfogad.
* **🏠 "My IP" Detektálás:** Ha a bemenetet üresen hagyjuk, a saját publikus IP címünk adatait kérdezi le.
* **🗺️ Google Maps Integráció:** A kapott koordináták (Latitude/Longitude) alapján generál egy kattintható térkép linket.
* **🛡️ Hibatűrés:** Beépített hibakezelés (Exception Handling) a hálózati problémák és API timeoutok esetére.
* **JSON Feldolgozás:** A szerver válaszát strukturált formában jeleníti meg.

## ⚙️ Technikai Részletek
* **Nyelv:** Python 3.x
* **Könyvtárak:** `requests` (HTTP hívásokhoz), `socket` (DNS feloldáshoz), `json`
* **API:** [ip-api.com](http://ip-api.com) (Nem igényel API kulcsot)

## 🚀 Telepítés & Használat

1. **Függőségek telepítése:**
   A program a `requests` modult használja. Ha nincs telepítve:
   ```bash
   pip install requests
