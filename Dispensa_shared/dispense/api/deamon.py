#funzione che cerca tutte gli gli Elementi in scadenza nei prossimi 7 giorni, ricava il prodotto e la dispensa di cui fanno parte
#e invia una mail a tutti gli utenti con cui è condivisa la dispensa
from datetime import datetime, timedelta
from dispense.models import Elementi, DispensaUser
from user.models import CustomUser



#funzione che scorre tutti gli utenti, per ogni utente controlla quali elementi ha in scadenza nei prossimi 7 giorni
#nelle varie dispense condivise con lui che hanni ul campo notifica abilitato
def checkScadenze():
    for user in CustomUser.objects.all():
        day = datetime.today()
        #TODO ERRORE nella query qui sotto
        #ricava tutti gli elementi in scadenza nei prossimi giorni dove l'elemento corrisponde ad un prodotto nelle dispense condivise con l'utente che hanno il campo notifica abilitato
        e = Elementi.objects.filter(data_scadenza__range=[day.strftime('%Y-%m-%d'), (day + timedelta(days=7)).strftime('%Y-%m-%d')]).order_by('id_prodotto__id_dispensa').order_by('data_scadenza')
        #prende le dispense che hanno il campo notifica abilitato e che hanno id_dispensa compreso negli elementi in scadenza
        dispense = DispensaUser.objects.filter(notifiche=True, id_dispensa__in=e.values('id_prodotto__id_dispensa').distinct())
        #filtra gli elementi in scadenza in modo che siano solo quelli che hanno id_dispensa compreso nelle dispense con campo notifica abilitato
        e = e.filter(id_prodotto__id_dispensa__in=dispense.values('id_dispensa'))

        #crea una lista di tuple (dispensa, prodotto, lista di elementi in scadenza in ordine di data scadenza)
        lista = []
        #se esiste almeno un elemento in scadenza
        if e.exists():
            #inserisce nella lista una tupla (dispensa, prodotto, lista di elementi in scadenza in ordine di data scadenza), 
            # dove tutti gli elementi fanno parte di prodotti all'interno di quella dispensa
            #per ogni elemento in scadenza

            #TODO implementare questo metodo
            #raggruppa tutti gli elementi e in un oggetto: (id_dispensa, [lista di oggetti, [lista di elementi in scadenza]])

            # for elem in e:
            #     #ricava il prodotto e la dispensa di cui fa parte
            #     prod = elem.id_prodotto
            #     disp = prod.id_dispensa
            #     #aggiunge una tupla per ogni tupla (id_dispensa, id_prodotto) diversa
            #     if (disp, prod) not in lista:
            #         lista.append((disp, prod, []))
            #     #aggiunge l'elemento in scadenza alla lista di elementi in scadenza della tupla corrispondente
            #     lista[lista.index((disp, prod, []))][2].append(elem)
            pass

                
            #per ogni tupla nella lista
        #stampa la lista
        for l in lista:
            #stampa il nome della dispensa
            #il nome del prodotto
            #e la lista di elementi in scadenza
            print(l[0].nome_dispensa)
            print(l[1].nome_prodotto)
            print(l[2])
            print()

    return



        




#Funzione che accetta un CustomUser e invia una mail con le api di django
def sendMail():
    send_mail()


def getProdotti():
    #ricava tutti gli elementi in scadenza nei prossimi 7 giorni
    e = Elementi.objects.filter(data_scadenza__range=[datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7)])
    if e.exists():
        #per ogni elemento in scadenza
        for elem in e:
            #ricava il prodotto e la dispensa di cui fa parte
            prod = elem.id_prodotto
            disp = prod.id_dispensa
            #ricava tutti gli utenti con cui è condivisa la dispensa e per ogni utente lo rica i dati dalla tabella user
            users = DispensaUser.objects.filter(id_dispensa=disp)
            for user in users:
                user = CustomUser.objects.get(id=user.id_user.id)
                send_mail(
                    'Scadenza prodotto',
                    'Il prodotto ' + prod.nome + ' scadrà tra 7 giorni',
                    [user.email],
                    fail_silently=False,
                )
    return
