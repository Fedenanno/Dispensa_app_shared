<template>
    <p> ID: {{ this.id }} |--</p>



    <div class="min-h-screen bg-gray-100 flex flex-col sm:py-12">
        <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md">
            <h1 class="text-2xl font-bold mb-6 text-center">Crea una nuova dispensa</h1>
            <form @submit.prevent="createDispensa" class="w-full max-w-sm mx-auto bg-white p-8 rounded-md shadow-md">
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="name">Nome</label>
                    <input v-model="name"
                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
                        type="text" id="name" name="name" placeholder="John Doe">
                </div>
                <div class="flex items-center mb-4">
                    <input id="default-checkbox" type="checkbox" value=""
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                    <label for="default-checkbox"
                        class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Condivisa
                        <a @click="showModalInfo = !showModalInfo" href="#"
                            class="text-indigo-600 hover:underline dark:text-blue-500"
                            data-modal-target="infoModal">(Info)</a>
                    </label>
                </div>
                <button
                    class="w-full bg-indigo-500 text-white text-sm font-bold py-2 px-4 rounded-md hover:bg-indigo-600 transition duration-300"
                    type="submit">Crea Dispensa
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                        class="w-4 h-4 inline-block">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M17 8l4 4m0 0l-4 4m4-4H3" />
                    </svg>
                </button>
            </form>
        </div>
    </div>
</template>


<script>

export default {
    name: 'prova',
    props: {
        id: {
            type: String,
            required: true
        },
    },
}
</script>
<style >
/* @import "@/style.css" */
</style>
