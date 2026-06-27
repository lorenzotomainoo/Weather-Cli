Weather CLI

Applicazione a riga di comando sviluppata in Python per la consultazione delle condizioni meteorologiche attuali e delle relative previsioni tramite le API di Visual Crossing Weather.
Funzionalità

    Rilevamento automatico della posizione tramite indirizzo IP.

    Ricerca meteorologica basata su specifica città.

    Visualizzazione di dati dettagliati: temperatura, umidità, velocità del vento e condizioni atmosferiche.

    Supporto per previsioni multi-giorno.

    Sistema di caching dei dati con validità di 30 minuti per l'ottimizzazione delle richieste API.

    Gestione sicura della chiave API tramite file di configurazione .env.

Tecnologie

    Python 3

    Requests

    python-dotenv

    Visual Crossing Weather API

Installazione

Clonare il repository:
Bash

git clone https://github.com/YOUR_USERNAME/weather-cli.git
cd weather-cli

Installare le dipendenze necessarie:
Bash

pip install -r requirements.txt

Configurazione

È necessario ottenere una chiave API dal portale Visual Crossing. Una volta ottenuta, creare un file denominato .env nella directory principale del progetto e inserire la chiave nel seguente formato:
Snippet di codice

API_KEY=tua_api_key

Utilizzo

L'applicazione supporta i seguenti comandi:

    Posizione corrente: python weather.py

    Ricerca per città: python weather.py --city NomeCittà

    Previsioni estese: python weather.py --city NomeCittà --day NumeroGiorni

Sono disponibili le seguenti abbreviazioni:

    -c per --city

    -d per --day

Struttura del Progetto
Plaintext

weather-cli/
│
├── cache/
│   └── .cache_city.json
├── .env
├── .gitignore
├── weather.py
├── README.md
└── requirements.txt

Caching

I dati meteorologici vengono archiviati temporaneamente nella directory cache/. I file salvati sono riutilizzati per un intervallo di 30 minuti al fine di limitare il numero di chiamate verso l'API.
Licenza

Il progetto è distribuito sotto licenza MIT.
