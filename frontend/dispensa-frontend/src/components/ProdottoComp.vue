<template>
    <div>
        <!-- <div class="relative p-4 w-full max-w-2xl h-full md:h-auto"> -->
        <!-- Modal content -->
        <!-- <div class="relative p-4 bg-white rounded-lg shadow dark:bg-gray-800 sm:p-5"> -->
        <!-- Modal header -->
        <!-- <div class="flex justify-between items-center pb-4 mb-4 rounded-t border-b sm:mb-5 dark:border-gray-600">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                        Update Product
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-toggle="updateProductModal">
                        <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                                clip-rule="evenodd"></path>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div> -->
        <!-- Modal body -->
        <!-- <form action="#">
                    <div class="grid gap-4 mb-4 sm:grid-cols-2">
                        <div>
                            <label for="name"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                            <input type="text" name="name" id="name" value="iPad Air Gen 5th Wi-Fi"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Ex. Apple iMac 27&ldquo;">
                        </div>
                        <div>
                            <label for="brand"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Brand</label>
                            <input type="text" name="brand" id="brand" value="Google"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Ex. Apple">
                        </div>
                        <div>
                            <label for="price"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                            <input type="number" value="399" name="price" id="price"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="$299">
                        </div>
                        <div>
                            <label for="category"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Category</label>
                            <select id="category"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500">
                                <option selected="">Electronics</option>
                                <option value="TV">TV/Monitors</option>
                                <option value="PC">PC</option>
                                <option value="GA">Gaming/Console</option>
                                <option value="PH">Phones</option>
                            </select>
                        </div>
                        <div class="sm:col-span-2">
                            <label for="description"
                                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                            <textarea id="description" rows="5"
                                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                                placeholder="Write a description...">Standard glass, 3.8GHz 8-core 10th-generation Intel Core i7 processor, Turbo Boost up to 5.0GHz, 16GB 2666MHz DDR4 memory, Radeon Pro 5500 XT with 8GB of GDDR6 memory, 256GB SSD storage, Gigabit Ethernet, Magic Mouse 2, Magic Keyboard - US</textarea>
                        </div>
                    </div>
                    <div class="flex items-center space-x-4">
                        <button type="submit"
                            class="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                            Update product
                        </button>
                        <button type="button"
                            class="text-red-600 inline-flex items-center hover:text-white border border-red-600 hover:bg-red-600 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900">
                            <svg class="mr-1 -ml-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                                xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd"
                                    d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                                    clip-rule="evenodd"></path>
                            </svg>
                            Delete
                        </button>
                    </div>
                </form>
            </div>
        </div> -->
    </div>

    <div v-if="this.prodotto != null" class="bg-white dark:bg-gray-800 rounded-lg shadow-lg mt-4">
        <div class="px-6 py-4">
            <h2 class="text-xl font-bold">{{ this.prodotto.nome_prodotto }}</h2>
        </div>
        <div class="flex items-center justify-between px-6 py-4">
            <div class="w-1/2">
                <img class="rounded-lg" src="https://picsum.photos/300/200" alt="Prodotto">
            </div>
            <div class="w-1/2 pl-4 border-l border-black dark:border-white">
                <!-- <h3 class="text-lg font-bold">{{ this.prodotto.nome_prodotto }}</h3> -->
                <p class="text-lg text-gray-800 dark:text-gray-300">Codice: <span class="text-gray-600 dark:text-gray-400">{{ this.prodotto.id_prodotto }}</span></p>
                <p class="text-lg text-gray-800 dark:text-gray-300">Descrizione: <span class="text-gray-600 dark:text-gray-400">{{ this.prodotto.descrizione_prodotto }}</span></p>
                <p class="text-lg text-gray-800 dark:text-gray-300">Marca: <span class="text-gray-600 dark:text-gray-400">{{ this.prodotto.marca_prodotto }}</span></p>
                <p class="text-lg text-gray-800 dark:text-gray-300">Prezzo: <span class="text-gray-600 dark:text-gray-400">{{ this.prodotto.prezzo }}</span></p>
                <p class="text-lg text-gray-800 dark:text-gray-300">Categoria: <span class="text-gray-600 dark:text-gray-400">{{ this.prodotto.categoria }}</span></p>
                <p class="text-lg text-gray-800 dark:text-gray-300">Inserito da: <span class="text-gray-600 dark:text-gray-400">{{ this.prodotto.inserito_da }}</span></p>
                
            </div>
        </div>
        <div v-show="this.mostra_elementi" class="px-6 py-4">
            <h4 class="text-lg font-bold">Elementi attivi:</h4>
            <div class="mt-2">
                <ElementoComp :id_dispensa="this.id_dispensa" :id_prodotto="this.id_prodotto" :image="false" />
            </div>
        </div>
        <div class="flex items-center justify-between px-6 py-4">
            <button @click="this.mostra_elementi = !this.mostra_elementi" class="text-gray border border-gray-300 hover:bg-orange-400 py-2 px-4 rounded-lg">
                {{ this.mostra_elementi ? 'Nascondi elementi' : 'Mostra elementi'  }}
            </button>
            <div class="space-x-2">
                
                <button v-if="this.confermaElimina" @click="this.confermaElimina = !this.confermaElimina" class="text-gray border bg-orange-400 border-orange-600 rounded-lg hover:bg-orange-400 py-2 px-4">
                    Annulla
                </button>
                <!-- <button v-else class="text-gray border border-gray-300 rounded-lg hover:bg-orange-400 py-2 px-4">
                    Modifica
                </button> -->
                
                <button v-if="this.confermaElimina" @click="this.eliminaProdotto" class="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded-lg">
                    Confermi eliminazione?
                </button>
                <button v-else @click="this.confermaElimina = !this.confermaElimina" class="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded-lg">
                    Elimina
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import { axios } from '@/common/axiosSetting'

//component
import ElementoComp from '@/components/ElementoComp.vue'
import { onUpdated } from 'vue'

export default {
    name: 'ProdottoComp',
    props: {
        id_dispensa: {
            type: [Number, String],
            required: true
        },
        id_prodotto: {
            type: [Number, String],
            required: true
        },
    },
    components: {
        ElementoComp
    },
    data() {
        return {
            prodotto: null,
            confermaElimina: false,

            //elementi
            mostra_elementi: false,
            //elementi: [],
        }
    },
    methods: {
        sendNotificaiont(type, message){
            this.$toast.open({
                message: message,
                type: type,
                position : 'top-left',
                dismissible: true,
                duration: 5000,
                pauseOnHover: true

            });
        },
        async getProdotto() {
            try {
                const response = await axios.get('dispense/' + this.id_dispensa + '/prodotti/' + this.id_prodotto + '/')
                this.prodotto = response.data[0]
            }
            catch (error) {
                this.sendNotificaiont('error', 'Errore durante il recupero del prodotto')
                console.log("!!!!!!errore!!!" + error)
            }
        },
        async eliminaProdotto(){
            try{
                const response = await axios.delete('dispense/' + this.id_dispensa + '/prodotti/' + this.id_prodotto + '/')
                this.prodotto = null
                this.confermaElimina = false
                this.sendNotificaiont('success', 'Prodotto eliminato con successo')
            }catch(error){
                this.sendNotificaiont('error', 'Errore durante l\'eliminazione del prodotto')
            }
        }
        // async getElementi() {
        //     try {
        //         const response = await axios.get('dispense/' + this.id_dispensa + '/prodotti/' + this.id_prodotto + '/elementi/')
        //         this.elementi = response.data
        //     }
        //     catch (error) {
        //         console.log("!!!!!!errore!!!" + error)
        //     }
        // },
    },
    beforeMount() {
        this.getProdotto()
    },
    updated() {
        this.getProdotto()
    }
}
</script>