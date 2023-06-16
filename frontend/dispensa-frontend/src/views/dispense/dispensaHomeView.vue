<template>
    <!-- pulsante back -->
    <div class="md:container md:mx-auto pb-2 pt-1">
        <router-link to="/">
            <button type="button"
                class="text-indigo-700 border border-indigo-700 hover:bg-indigo-700 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm p-2.5 text-center inline-flex items-center mr-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:focus:ring-blue-800 dark:hover:bg-blue-500">
                <svg class="w-5 h-5" height="512px" id="Layer_1" style="enable-background:new 0 0 512 512;" version="1.1"
                    viewBox="0 0 512 512" width="512px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink">
                    <polygon points="352,128.4 319.7,96 160,256 160,256 160,256 319.7,416 352,383.6 224.7,256 " />
                </svg>
                <span class="sr-only">Icon description</span>
            </button>

        </router-link>
    </div>

    <!-- pulsantiera cambia visualizzazione -->
    <div class="flex items-center justify-center pb-10">
        <div class="inline-flex rounded-md shadow-sm" role="group">
            <div class="inline-flex rounded-md shadow-sm" role="group">
                <button @click="this.visualizza = 'elementi'" type="button"
                    class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-l-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                    <svg aria-hidden="true" class="w-4 h-4 mr-2 fill-current" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
                            clip-rule="evenodd"></path>
                    </svg>
                    Elementi
                </button>
                <button @click="this.modal_aggiunta.show()" type="button"
                    class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border-t border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                    <svg aria-hidden="true" class="w-4 h-4 mr-2 fill-current" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z">
                        </path>
                    </svg>
                    Aggiungi
                </button>
                <button @click="this.visualizza = 'prodotti'" type="button"
                    class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-r-md hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                    <svg aria-hidden="true" class="w-4 h-4 mr-2 fill-current" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z"
                            clip-rule="evenodd"></path>
                    </svg>
                    Prodotti
                </button>
            </div>
        </div>
    </div>

    <!-- Prodotti in scadenza -->
    <div v-if="this.visualizza == 'elementi'" class="md:container md:mx-auto pb-10">

        <!-- Prodotti in scadenza oggi -->
        <h2 class="text-4xl font-extrabold dark:text-white">Prodotti in scadenza
            <span class="underline underline-offset-3 decoration-8 decoration-blue-400 dark:decoration-blue-600">oggi.
            </span>
        </h2>
        <!-- elementi -->
        <ElementoComp :id_dispensa="this.id" :data_ricerca="data_oggi()" :key="this.componentKey" />


        <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 ">

        <!-- Prodotti in scadenza oggi -->

        <div class="md:container md:mx-auto flex items-center">
            <h2 class="text-4xl font-extrabold dark:text-white inline">Prodotti in scadenza:
                <span class="underline underline-offset-3 decoration-8 decoration-blue-400 dark:decoration-blue-600">{{
                    (elementi_data) ? this.dateValue['undefined'] + '.' : "" }}
                </span>
            </h2>
            <div class="relative ml-4">
                <vue-tailwind-datepicker as-single placeholder="Scegli data"
                    :formatter="{ date: 'DD-MM-YYYY', month: 'MMM' }" v-model="dateValue" />
            </div>
        </div>
        <!-- elementi data scelta-->
        <ElementoComp v-if="this.elementi_data" :id_dispensa="this.id" :data_ricerca="this.dateValue['undefined']" />


        <!-- prodotti -->
        <!-- <div class="grid gap-4 grid-cols-3 pt-6"> -->
        <!-- aggiungere v-for -->
        <!-- <div v-for="prd in prodotti_data">
                <ProdottoComp :id_dispensa="this.id" :id_prodotto="prd.id_prodotto" />
            </div>
        </div> -->
    </div>

    <!-- Aggiungi nuovo prodotto / elemento -->
    <div id="modal_aggiunta" tabindex="-1" aria-hidden="true"
        class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative w-full max-w-md max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <button @click="this.modal_aggiunta.hide()" type="button"
                    class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-800 dark:hover:text-white"
                    data-modal-hide="">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>

                <div class="px-6 py-6 lg:px-8">
                    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Aggiungi un nuovo Prodotto / Elemento
                        TODO sistemare il fatto che non si puo creare un prodotto e aggiungere subito un elemento, non fa in tempo o cmq ce un errore
                    </h3>

                    <form class="space-y-4" @submit.prevent="this.aggiuntiProdottoElemento">

                        <div>
                            <label for="codice_prodotto"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white ">Codice
                                prodotto</label>
                            <input v-model="this.nuovo_prodotto.id_prodotto" type="number" id="codice_prodotto"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                placeholder="name@company.com" required>
                        </div>
                        <div v-if="!this.prodotto_esistente">
                            <div>
                                <label for="nome_prodotto"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white ">Nome</label>
                                <input v-model="this.nuovo_prodotto.nome_prodotto" type="string" name="number"
                                    id="nome_prodotto"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                    placeholder="name@company.com" required>
                            </div>
                            <div>
                                <label for="descrizione_prodotto"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white mt-3">Descrizione</label>
                                <input v-model="this.nuovo_prodotto.descrizione_prodotto" type="string"
                                    id="descrizione_prodotto"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                    placeholder="name@company.com">
                            </div>
                            <div>
                                <label for="marca_prodotto"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white mt-3">Marca</label>
                                <input v-model="this.nuovo_prodotto.marca_prodotto" type="string" name="number"
                                    id="marca_prodotto"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                    placeholder="name@company.com">
                            </div>
                            <div>
                                <label for="prezzo_prodotto"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white mt-3">Prezzo</label>
                                <input v-model="this.nuovo_prodotto.prezzo" type="number" name="number" id="prezzo_prodotto"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                    placeholder="name@company.com">
                            </div>
                            <div>
                                <label for="countries"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white mt-3">Categoria</label>
                                <select v-model="this.nuovo_prodotto.id_categoria" id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    required>
                                    <option selected>Choose a country</option>
                                    <option value="1">United States</option>
                                    <option value="CA">Canada</option>
                                    <option value="FR">France</option>
                                    <option value="DE">Germany</option>
                                </select>
                            </div>
                        </div>
                        <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700 " />

                        <!-- Aggiunta elemento -->
                        <div class="relative ">
                            <vue-tailwind-datepicker as-single placeholder="Scegli data"
                                :formatter="{ date: 'DD-MM-YYYY', month: 'MMM' }" v-model="this.data_nuovo_elemento"
                                required />
                        </div>
                        <div class="flex justify-between">

                            <a href="#" class="text-sm text-blue-700 hover:underline dark:text-blue-500">Serve aiuto?</a>
                        </div>

                        <!-- pulsanti finali modal -->
                        <div class="flex space-x-5 justify-center">
                            <button type="submit"
                                class="flex items-center justify-center w-40 h-10 text-gray border border-gray-300 rounded-lg hover:bg-green-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                Aggiungi
                            </button>
                            <button @click="this.modal_aggiunta.hide()" type="button"
                                class="flex items-center justify-center w-40 h-10 text-gray border border-gray-300 rounded-lg hover:bg-red-400 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                Annulla
                            </button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- cerca / mostra lista prodotti -->
    <div v-if="this.visualizza == 'prodotti'" class="md:container md:mx-auto pb-10">
        <form @submit.prevent="">
            <label for="default-search"
                class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
            <div class="relative">
                <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none"
                        stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                    </svg>
                </div>
                <input v-model="this.ricerca" type="search" id="default-search"
                    class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Search Mockups, Logos..." required>
                <button type="submit"
                    class="text-white absolute right-2.5 bottom-2.5 bg-indigo-700 hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
            </div>
        </form>

        <!-- prodotti -->
        <div v-for="prd in prodotti">
            <ProdottoComp :id_dispensa="prd.id_dispensa" :id_prodotto="prd.id_prodotto" />
        </div>
    </div>
</template>


<script>
import { axios } from '@/common/axiosSetting'
//components
import ProdottoComp from '@/components/ProdottoComp.vue'
import ElementoComp from '@/components/ElementoComp.vue'
//css
import { Modal } from 'flowbite'
import { ref } from 'vue';


export default {
    setup() {

    },
    name: 'dispensaHomeView',
    props: {
        id: { //id della dispensa
            type: String,
            required: true
        },
    },
    components: {
        ProdottoComp,
        ElementoComp,
    },
    data() {
        return {
            //per elementi
            dateValue: new Date(), //data scelta per la ricerca degli elementi
            elementi_data: false, //indica se è stata inserita una data per la ricerca degli elementi
            //per prodotti
            prodotti: [], //prodotti nella dispensa
            prodotti_data: [],
            visualizza: 'elementi', //serve per visualizzare il menu corretto
            ricerca: '', //valore del campo ricerca
            //aggiunta prodotti elementi
            nuovo_prd_el: false,
            prodotto_esistente: true, //indica se il prodotto esiste gia nella dispensa (viene modificato da una GET)
            modal_aggiunta: null, //oggetto modal per laggiunta
            nuovo_prodotto: {
                id_dispensa: this.id
            }, //dati del nuovo prodotto da aggiungere
            data_nuovo_elemento: new Date(), //data del nuovo elemento da aggiungere
            //aggiorna compo
            componentKey: ref(0),
        }
    },
    methods: {
        async getProdotti() {
            try {
                const response = await axios.get('dispense/' + this.id + '/prodotti/')
                this.prodotti = response.data
            } catch (e) {
                console.log(e)
            }
        },
        async getProdottiData() { },
        data_oggi() {
            //data di oggi nel formato dd-mm-yyyy in un unica riga
            return new Date().toLocaleDateString().replaceAll("/", "-")//.split("/").reverse().join("-")
        },
        cercaProdotto(string) {
            //prende tutti gli elementi in prodotti in cui string è una sottostringa del nome_prodotto e crea un nuovo Array
            this.prodotti = this.prodotti.filter(el => el.nome_prodotto.includes(string))
        },
        async aggiuntiProdottoElemento() {
            //controllo se esiste l'elemento con una get
            if (this.prodotto_esistente)
                try {
                    const url = 'dispense/' + this.id + '/prodotti/' + this.nuovo_prodotto.id_prodotto + "/"
                    console.log("url: " + url)
                    const response = await axios.get(url)
                    //axios resistuisce lo status solo se fallisce, quindi nel catch
                    // if (response.status >= 400 && response.status < 600) {
                    //     this.prodotto_esistente = false
                    //     return
                    // }
                    console.log("prodotto esiste: " + response.status)
                } catch (e) {
                    this.prodotto_esistente = false
                    console.log("prodotto non esiste")
                    return
                }
            //se non esiste apro il menu e lo faccio creare con una post
            else {
                if (this.nuovoProdotto() < 300) {
                    this.prodotto_esistente = true
                    console.log("prodotto aggiunto")
                }
            }

            //infine controllo se la data elemento != data di default, se si, aggiungo pure l'elemento
            if (this.data_nuovo_elemento.toString().split('').length < 16 && this.data_nuovo_elemento['undefined'].length != 0) {
                try {
                    const response = await axios.post('dispense/' + this.id + '/prodotti/' + this.nuovo_prodotto.id_prodotto + "/elementi/", {
                        data_scadenza: this.data_nuovo_elemento['undefined'].split("-").reverse().join("-"),
                        id_prodotto: this.nuovo_prodotto.id_prodotto
                    })
                    // ricarico il componente che visualizza gli elementi scaduti, dopo l'aggiunta di un nuovo elemento
                    this.forceRerender()

                } catch (e) { console.log("errore aggiunta elemento: " + e) }
            }
        },
        forceRerender() {
            this.componentKey += 1;
        },

        async nuovoProdotto() {
            //aggiunge un nuovo prodotto
            try {
                const response = await axios.post('dispense/' + this.id + '/prodotti/', /*payload*/  this.nuovo_prodotto)
                return response.status
            } catch (e) {
                console.log("Aggiunta prodotto: ")
                '404'
            }
        }
    },
    beforeMount() {
        this.getProdotti()
    },
    mounted() {
        // modal aggiunta prodotti / elementi
        const $modalElementInfo = document.querySelector('#modal_aggiunta');
        const modalOptions = { backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40' }
        this.modal_aggiunta = new Modal($modalElementInfo, modalOptions);
    },
    watch: {
        dateValue: function (val, newVal) {

            if (newVal.toString().split('').length > 16)
                this.elementi_data = true
            else if (this.dateValue['undefined'].length == 0)
                this.elementi_data = false
        },
        ricerca: function (val, newVal) {
            if (newVal.length == '')
                this.getProdotti()
            else
                this.cercaProdotto(newVal)
        },

    }
}
</script>

<style >
@import "@/style.css"
</style>