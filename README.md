# Dispensa_app_shared

Progetto sotto sviluppo, alcune funzioni potrebbero non essere ancora state implementate.

Applicativo online sviluppato per dispositivi fissi e mobili (work in progress) che si occupa di gestire una dispensa alimentare condivisa tra utenti. Ogni utente dopo la registrazione (o login) può interagire con le proprie dispense o con quelle condivide da degli utenti. Possono essere dati dei ruoli (admin o user) in modo da limitare i permessi nella modifica / rimozione di alimenti. Il progetto inizale nasce come risposta allo spreco alimentare durante la convivenza universitaria, inizialmente ogni dispensa ha i suoi prodotti specifici che possono essere aggiunti, modificati o eliminati, ora però il progetto si sta muovendo verso un approccio più centralizzato dove cè un pool di prodotti a cui ogni utente può accedere e importare nella propria dispensa, questo è stato pensato per l’aggiunta futura di nuove funzioni come il consiglio di recette in base a cos’e in scadenza. L’applicativo ricorda tramite mail o notifica push gli elementi in scadenza in data odierna e fa un recap ogni settimana. 

> How to run
> 

Back-end in DRF (python)

Login con token grazie a know

django run on port 8000

Front-end in vue.js

vue run on port ….

Windows:

```java
Django;
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

intall vue
npm create vite@latest

run
npm install
npm run dev

for  tailwind
comandi della doc. ufficiale
for tailwind template
npm install @headlessui/vue @heroicons/vue
```