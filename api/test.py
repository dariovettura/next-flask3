from flask import Blueprint, request, jsonify
import requests
from bs4 import BeautifulSoup
import urllib.parse  

# Creazione del blueprint per il nuovo endpoint
test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["POST"])
def test():
    # Ottieni i dati JSON dal corpo della richiesta
    data = request.get_json()
    
    # Estrai i parametri dal JSON
    checkin = data.get('checkin')
    checkout = data.get('checkout')
    pax = data.get('pax')

    # Controlla che tutti i parametri siano presenti
    if not checkin or not checkout or not pax:
        return jsonify({"error": "Parametri mancanti: checkin, checkout e pax sono richiesti."}), 400

    # Costruisci il link con i parametri forniti
    base_url = "https://book.octorate.com/octobook/site/reservation/result.xhtml"
    query_params = {
        "checkin": checkin,
        "checkout": checkout,
        "pax": pax,
        "codice": "92196"  # codice fisso
    }

    # Aggiungi i parametri di query all'URL
    full_url = f"{base_url}?{urllib.parse.urlencode(query_params)}"
    print(f"Link completo costruito: {full_url}")  # Stampa per debug

    # Effettua la richiesta GET al link costruito
    response = requests.get(full_url)
    
    if response.status_code == 200:
        # Parsing del contenuto HTML con BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Trova tutti i div con la classe RoomSection
        room_sections = soup.find_all('div', class_='RoomSection')

        # Lista per raccogliere le informazioni delle stanze
        rooms = []

        # Cicla attraverso ogni sezione trovata
        for section in room_sections:
            room_info = {}

            # Estrai l'intestazione della stanza (h1)
            room_name_tag = section.find('h1')
            room_info['name'] = room_name_tag.text.strip() if room_name_tag else 'N/A'

            # Estrai altre informazioni basate su elementi specifici
            room_info['size'] = section.find('span').text.strip() if section.find('span') else 'N/A'

            # Estrai i servizi dal paragrafo (p) che contiene immagini e testo
            services_paragraphs = section.find_all('p')
            services = []
            if services_paragraphs:
                for serv in services_paragraphs:
                    services.extend([service.strip() for service in serv.text.strip().split(" - ") if service.strip()])
                room_info['services'] = list(set(services))  # Rimuovi duplicati
            else:
                room_info['services'] = []

            # Descrizione breve (shortDesc) e descrizione dettagliata
            short_desc_tag = section.find('div', class_='shortDesc')
            room_info['short_description'] = short_desc_tag.text.strip() if short_desc_tag else 'N/A'

            detailed_desc_tag = section.find('div', class_='RoomBottom roominfo')
            room_info['detailed_description'] = detailed_desc_tag.text.strip() if detailed_desc_tag else 'N/A'

            # Aggiungi le informazioni raccolte alla lista delle stanze
            rooms.append(room_info)

        # Ritorna il risultato in formato JSON
        return jsonify({"rooms": rooms}), 200
    else:
        print(f"Errore nella richiesta: {response.status_code}")
        return jsonify({"error": f"Errore nella richiesta: {response.status_code}"}), response.status_code
