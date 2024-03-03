import { defineStore } from 'pinia'
import { axios } from '@/common/axiosSetting'

function setHeader(token) {
    //in caso di token vuoto, rimuove l'header altrimenti django restituisce 403
    if (token === '')
        delete axios.defaults.headers.common["Authorization"];
    else
        axios.defaults.headers.common['Authorization'] = `Token ${token}`
}

async function tryToken() {
    try {
        const response = await axios.get('dispense/')
        if (response.status < 300 || response.status >= 200) {
            console.log("token valido")
            return true
        }
    }
    catch (error) {
        console.log("token non valido")
        return false
    }
}

export const useAuthStore = defineStore('auth', {
    state: () => ({
        authUser: null,
    }),
    getters: {
        user: (state) => state.authUser,
        isAuthenticated: (state) => !!state.authUser,
    },
    actions: {
        async getUser() {
            if (localStorage.getItem('user')) {
                this.authUser = JSON.parse(localStorage.getItem('user'))
                setHeader(this.authUser.token)
                //controllo se il token è sempre valido, in caso negativo, eseguo il logout
                const tokenValido = await tryToken()
                if (!tokenValido) {
                    this.removeUser()
                    console.log("token non valido, rimuovo utente")
                    return null;
                }
                else
                    return this.authUser
            }
        },
        async login(username, password) {
            
            try {
                const response = await axios.post('auth/login', {
                    username,
                    password,
                })
                this.authUser = response.data.user
                localStorage.setItem('user', JSON.stringify(response.data))
                setHeader(response.data.token)
                return true
            }
            catch (error) {
                return false
            }
        },
        async register(username, email, password) {
            try {
                const response = await axios.post('auth/register', {
                    username,
                    email,
                    password,
                })
                //this.authUser = response.data.user
                return response
            }
            catch (error) {
                if(error.response)
                    console.log("errore in reg: "+ error.response)
            }
        },
        async logout() {
            try {
                const response = await axios.post('auth/logout')
                this.authUser = null
                setHeader('')
                localStorage.removeItem('user')
                console.log("Eseguito logout")
                return response
            }
            catch (error) {
                throw error
            }
        },
        async logoutAll() {
            try {
                const response = await axios.post('auth/logoutAll')
                this.authUser = null
                setHeader('')
                localStorage.removeItem('user')
                return response
            }
            catch (error) {
                throw error
            }
        },
        removeUser() {
            this.authUser = null
            setHeader('')
            localStorage.removeItem('user')
        }
    },
})

