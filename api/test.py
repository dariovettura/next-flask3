from flask import Blueprint, request, jsonify
import requests
from bs4 import BeautifulSoup
import urllib.parse  # Import per codificare l'URL

# Creazione del blueprint per il nuovo endpoint
test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["GET", "POST"])
def test():
    # Controlla se è una richiesta GET o POST
    if request.method == "GET":
        # Ottieni il parametro 'link' dall'URL
        link = request.args.get('link')
        pax = request.args.get('pax')
        codice = request.args.get('codice')
        checkout = request.args.get('checkout')
    elif request.method == "POST":
        # Ottieni i dati JSON dal corpo della richiesta
        data = request.get_json()
        link = data.get('link')
        pax = data.get('pax')
        codice = data.get('codice')
        checkout = data.get('checkout')

    # Verifica che il link esista
    if not link:
        return jsonify({"error": "Nessun link fornito"}), 400

    # Costruisci i parametri per l'URL
    query_params = {
        "pax": pax,
        "codice": codice,
        "checkout": checkout
    }

    # Aggiungi i parametri di query all'URL
    full_url = f"{link}&{urllib.parse.urlencode(query_params)}"
    print(f"Link completo costruito: {full_url}")  # Stampa per debug

    # Effettua la richiesta GET al link costruito
    response = requests.get(link)
    
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
    else:
        print(f"Errore nella richiesta: {response.status_code}")
        return jsonify({"error": f"Errore nella richiesta: {response.status_code}"}), response.status_code
