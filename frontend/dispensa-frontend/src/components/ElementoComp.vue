<template>
    <!-- elementi -->
    <div v-if="edit_data.length > 0" class="grid gap-4 grid-cols-3 pt-6">

        <div v-for="(el, index) in elementi">
            <div
                class="mb-3 w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 ">
                <!-- dropdown -->
                <!-- <div class="flex justify-end px-4 pt-4">
                    <button :id="'dropdownButton' + this.randomSlugDropdown" :data-dropdown-toggle="'dropdown_' + this.randomSlugDropdown"
                        class="inline-block text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-1.5"
                        type="button">
                        <span class="sr-only">Open dropdown</span>
                        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path
                                d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z">
                            </path>
                        </svg>
                    </button>
                    Dropdown menu
                    <div :id="'dropdown_' + this.randomSlugDropdown" 
                        class="z-10 hidden text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                        <ul v-if="!edit_data[index]" class="py-2" :aria-labelledby="'dropdownButton' + this.randomSlugDropdown">
                            <li>
                                <a @click="edit_data[index] = true"
                                    href="#"
                                    
                                    class="block px-4 py-2 text-sm text-gray-700 hover:text-orange-400 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">
                                    Modifica</a>
                            </li>
                            <li>
                                <a @click="this.deleteElemento(el.id_prodotto.id_prodotto, el.id_elemento)"
                                    href="#"
                                    class="block px-4 py-2 text-sm text-gray-700 hover:text-red-600 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">
                                    Elimina</a>
                            </li>
                        </ul>
                    </div>
                </div> -->
                <!-- info -->
                <div class="flex flex-col items-center pb-6 px-4 pt-4">
                    <!-- immagine -->
                    <img v-show="this.image" class="w-24 h-24 mb-3 rounded-full shadow-lg" src="#" alt="Bonnie image" />
                    <!-- info -->
                    <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">{{ el.id_prodotto.nome_prodotto }}</h5>
                    <span class="text-sm text-gray-500 dark:text-gray-400">Codice: {{ el.id_prodotto.id_prodotto }}</span><br>
                    <span class="text-sm text-gray-900 dark:text-gray-400">Scadenza: {{ el.data_scadenza }}</span>
                    <!-- data -->
                    <div v-show="edit_data[index]" class="relatieve p-2 mt-3">
                        <vue-tailwind-datepicker class="absolute inset-y-0 right-0 w-16" as-single placeholder="Scegli data"
                            :formatter="{ date: 'DD-MM-YYYY', month: 'MMM' }" v-model="date_value" />
                    </div>
                    <!-- pulsanti -->
                    <div class="flex mt-2 space-x-3 relative md:mt-6">
                        <!-- conferma modifica -->
                        <div v-if="edit_data[index]">
                            <a @click="edit_data[index] = false" href="#"
                                class="mr-3 inline-flex items-center px-4 py-2 text-sm font-medium text-center text-gray-900 bg-white border border-gray-300 rounded-lg hover:bg-orange-400 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-700">
                                Annulla</a>
                            <a @click="this.editElemento(el.id_prodotto, el.id_elemento, index)" href="#"
                                class=" inline-flex items-center px-4 py-2 text-sm font-medium text-center text-gray-900 bg-white border border-gray-300 rounded-lg hover:bg-green-400 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-700">
                                Conferma</a>
                        </div>
                        <div v-else>
                            <a @click="edit_data[index] = true" href="#"
                                class="mr-2 inline-flex items-center px-4 py-2 text-sm font-medium text-center text-gray-900 bg-white border border-gray-300 rounded-lg hover:bg-orange-400 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-700">
                                Modifica</a>
                            <a @click="this.deleteElemento(el.id_prodotto, el.id_elemento)" href="#"
                                class="inline-flex items-center px-4 py-2 text-sm font-medium text-center text-gray-900 bg-white border border-gray-300 rounded-lg hover:bg-red-400 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-700 dark:focus:ring-gray-700">
                                Elimina</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- nessun elemento presente -->
    <div v-else class="md:container pt-8">
        <p class="text-center text-gray-500 dark:text-gray-400">Nessun elemento {{ (id_prodotto != null) ? "con il codice fornito" : " in data: "+this.data_ricerca }}</p>
    </div>
</template>

<script>
import { axios } from '@/common/axiosSetting'

export default {
    name: 'ElementoComp',
    props: {
        id_dispensa: {
            type: [Number, String],
            required: true
        },
        id_prodotto: {
            type: [Number, String],
        },
        data_ricerca: {
            type: String,
        },
        image: {
            type: Boolean,
            default: true
        }
    },
    components: {
    },
    data() {
        return {
            elementi: [],
            //viene utilizzato per gestire la grafica della modifica
            edit_data: [],
            date_value: new Date(),
            randomSlugDropdown: (Math.random() + 1).toString(36).substring(7)
        }
    },
    methods: {
        getElementi() {
            if (this.data_ricerca != null) {
                this.getElementiInScadenza();
            }
            else if (this.id_prodotto != null) {
                this.getElementiProdotto();
            }
        },
        //prende gli elementi in base alla scadenza
        getElementiInScadenza() {
            try {
                //invertire la data: .split("-").reverse().join("-")
                axios.get('/dispense/' + this.id_dispensa + '/prodotti/elementi/' + this.data_ricerca.split("-").reverse().join("-") + '/')
                    .then(response => {
                        // inizializza l'array edit_data con tutti valori false per quanti elementi sono presenti in elementi
                        this.edit_data = new Array(response.data.length).fill(false);
                        this.elementi = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            } catch (error) { }
        },
        //prende gli elementi in base all'id del prodotto
        getElementiProdotto() {
            //invertire la data: .split("-").reverse().join("-")
            axios.get('/dispense/' + this.id_dispensa + '/prodotti/' + this.id_prodotto + '/elementi/')
                .then(response => {
                    // inizializza l'array edit_data con tutti valori false per quanti elementi sono presenti in elementi
                    this.edit_data = new Array(response.data.length).fill(false);
                    this.elementi = response.data;


                })
                .catch(error => {
                    console.log(error);
                });

        },
        //Modifica un elemento di un prodotto
        editElemento(id_prodotto, id_elemento, indice) {
            if(this.data_ricerca){
                id_prodotto = id_prodotto.id_prodotto
            }
            console.log(id_prodotto)
            const url = '/dispense/' + this.id_dispensa + '/prodotti/' + id_prodotto + '/elementi/' + id_elemento + '/'
            axios.put(url, {
                data_scadenza: this.date_value['undefined'].split("-").reverse().join("-"),
            })
            .then(response => {
                this.getElementi();
            })
            .catch(error => {
                console.log("errore modifica elemento" + error);
            });

        },
        deleteElemento(id_prodotto, id_elemento) {
            if(this.data_ricerca){
                id_prodotto = id_prodotto.id_prodotto
            }
            axios.delete('/dispense/' + this.id_dispensa + '/prodotti/' + id_prodotto + '/elementi/' + id_elemento + '/')
            .then(response => {
                this.getElementi();
                this.toggleDropdown();
            })
            .catch(error => {
                console.log("errore elimina elemento" + error);
            });

        },
        toggleDropdown() {
            // Nasconde il dropdown
            this.$nextTick(() => {
                const dropdown = document.getElementById('dropdown_' + this.randomSlugDropdown);
                if (dropdown) {
                dropdown.classList.add('hidden');
                }
            });
        },

    },
    mounted() {
        this.getElementi();
        console.log("elementi: "+this.elementi)

    }
}

</script>