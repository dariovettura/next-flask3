from flask import Blueprint, request, jsonify
import requests
from bs4 import BeautifulSoup

# Creazione del blueprint per il nuovo endpoint
test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["POST"])
def test():
    # Ottieni i dati JSON dalla richiesta
    data = request.get_json()

    # Verifica che ci sia il campo 'link'
    if not data or 'link' not in data:
        return jsonify({"error": "Nessun link fornito"}), 400
    
    link = data['link']
    
    try:
        # Effettua una richiesta GET alla pagina specificata
        response = requests.get(link)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Errore nella richiesta: {str(e)}"}), 500

    # Parsing del contenuto HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

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
        services_paragraph = section.find('p')
        if services_paragraph:
            services = services_paragraph.text.strip().split(" - ")
            room_info['services'] = [service.strip() for service in services]
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
