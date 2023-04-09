# Werkplaats 3 
Dit is onze web-applicatie voor het inchecken van studenten die gebruik maakt van een RESTFUL API.

### Dit project is gemaakt met:
- Flask
- JavaScript
- Jinja2
- HTML
- CSS
- AJAX

### Functionaliteiten:

- **Studenten :**

   Studenten kunnen zichzelf inchecken, afmelden & een QR code scannen

- **Docenten :**

   Kunnen inloggen.  

   Kunnen een meeting aanmaken, de aanwezigheid van een student aanpassen, een vraag stellen via het inchecken & een QR code genereren per meeting.    

   Hebben een overzicht van de aanwezigheid van studenten per meeting, een overzicht met alle meetings & kan de antwoorden van de studenten zien per meeting.

- **Docent met admin rechten :**

    Kan admin rechten toewijzen aan een andere docent. 
    
    Kan studenten, klassen en docenten toevoegen & studenten, klassen en docenten "verwijderen".  

    Kan de database aanpassen.

## :warning: LET OP!!! :biohazard:
Voor het testen van de QR scan vervang ```if __name__ == "__main__":``` met:
```
if __name__ == "__main__":
     ctx = ('zeehond.crt', 'zeehond.key')
    # app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG)
    app.run(host=FLASK_IP, port=FLASK_PORT, debug=FLASK_DEBUG, ssl_context=ctx)
```
De camera functionaliteit kan niet aangezet worden als het via http gaat, dus verander http naar https nadat de bovenstaande code is vervangen.

Je browser gaat waarschijnlijk ook een melding geven dat de verbinding niet veilig is, omdat de certificaten self-signed zijn. Klik op ```Geavanceerd``` en daarna op ```Doorgaan naar <url> (onveilig) (Chrome) / Het risico aanvaarden (Firefox)``` .  

<sub>~~er wordt geen malware geïnstalleerd, trust me~~</sub>

## Om deze webapplicatie te starten doe het volgende:
```
pip install virtualenv
virtualenv venv
.\venv\scripts\activate
pip install -r requirements.txt

.\venv\scripts\activate
python app.py
```

.env bestand van hier downloaden :https://cdn.discordapp.com/attachments/1069646658205388953/1082771881423290398/env en in de root folder plakken.