# Dispensa_app_shared
![Dispensa](frontend/dispensa-frontend/public/icon_pwa/512_icon.png "Logo Dispensa")


## TOC
- [Dispensa_app_shared](#dispensa_app_shared)
  - [Introduzione](#introduzione)
  - [Tecnologie Utilizzate - How its work](#tecnologie-utilizzate---how-its-work)
    - [Back-end in DRF (python):](#back-end-in-drf-python)
    - [Front-end in vue.js:](#front-end-in-vuejs)
  - [Come installare l'app](#come-installare-lapp)
    - [Windows:](#windows)
      - [Django - Backend:](#django---backend)
      - [Vue - frontend:](#vue---frontend)
      - [For Tailwind:](#for-tailwind)
      - [For Tailwind Template:](#for-tailwind-template)

***

>#### Progetto sotto sviluppo, alcune funzioni potrebbero non essere ancora state implementate.

## Introduzione
Applicativo online sviluppato per dispositivi fissi e mobili (work in progress) che si occupa di gestire una dispensa alimentare condivisa tra utenti. Ogni utente dopo la registrazione (o login) può interagire con le proprie dispense o con quelle condivide da degli utenti. (work in progress) Possono essere dati dei ruoli (admin o user) in modo da limitare i permessi nella modifica / rimozione di alimenti. Il progetto inizale nasce come risposta allo spreco alimentare durante la convivenza universitaria, inizialmente ogni dispensa ha i suoi prodotti specifici che possono essere aggiunti, modificati o eliminati, (work in progress) ora però il progetto si sta muovendo verso un approccio più centralizzato dove cè un pool di prodotti a cui ogni utente può accedere e importare nella propria dispensa, questo è stato pensato per l’aggiunta futura di nuove funzioni come il consiglio di recette in base a cos’e in scadenza. (work in progress) L’applicativo ricorda tramite mail o notifica push gli elementi in scadenza in data odierna e fa un recap ogni settimana. 

## Tecnologie Utilizzate - How its work


>Back-end in DRF (python):
- Login tramite token (gestito dalla libreria KNOX) (WIP -> passaggio a JWT)
- Login tramite Oauth (Gestito tramite firebase) (WIP)
- Gestione notifiche app-onlne (Tramite web socket e Redis)
- Gestione notifiche app-offline (Tramite FCM) (WIP)
- Database basato su Postgre


>Front-end in vue.js:
- Store basato su Pinia
- PWA basata su Vite-PWA
- Http basato su Axios

---
### Come installare l'app

>Windows:

**Django - Backend:**
```shell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
---

**Vue - frontend:**
```shell
intall vue
npm create vite@latest

run
npm install
npm run dev
```

for  tailwind:
```shell
comandi della doc. ufficiale
```
for tailwind template:
```shell
npm install @headlessui/vue @heroicons/vue
```