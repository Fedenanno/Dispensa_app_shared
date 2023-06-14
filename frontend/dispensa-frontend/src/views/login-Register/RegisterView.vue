<template>
    <div class="min-h-screen bg-gray-100 flex flex-col sm:py-12">
        <div class="p-10 xs:p-0 mx-auto md:w-full md:max-w-md">
            <h1 class="text-2xl font-bold mb-6 text-center">Registration Form</h1>
            <form @submit.prevent="register" class="w-full max-w-sm mx-auto bg-white p-8 rounded-md shadow-md">
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="name">Name</label>
                    <input v-model="name"
                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
                        type="text" id="name" name="name" placeholder="John Doe">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="email">Email</label>
                    <input v-model="email"
                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
                        type="email" id="email" name="email" placeholder="john@example.com">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
                    <input v-model="password"
                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
                        type="password" id="password" name="password" placeholder="********">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="confirm-password">Confirm
                        Password</label>
                    <input v-model="confirmPassword"
                        class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500"
                        type="password" id="confirm-password" name="confirm-password" placeholder="********">
                </div>
                <button
                    class="w-full bg-indigo-500 text-white text-sm font-bold py-2 px-4 rounded-md hover:bg-indigo-600 transition duration-300"
                    type="submit">Register
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
import { useAuthStore } from '../../stores/auth'
import router from '@/router/index'

export default {
    name: 'RegisterView',
    data() {
        return {
            name: '',
            email: '',
            password: '',
            confirmPassword: '',
        }
    },
    methods: {
        async register() {
            if (this.password !== this.confirmPassword) {
                console.log("conferma password errata!")
                return;
            }
            await useAuthStore().register(this.name, this.email, this.password);
            router.push('/login');
        }
    }

}

</script>