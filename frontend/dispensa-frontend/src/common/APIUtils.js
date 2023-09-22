import { axios } from '@/common/axiosSetting'

//DISPENSE



//PRODOTTI
export async function getProdotti(id_dispensa) {
    try {
        const response = await axios.get('dispense/' + id_dispensa + '/prodotti/')
        return response
    } catch (e) {
        console.log(e)
    }
    
}


//ricerca
export async function getProdottiRicerca(id_dispensa, id_nome) {
    try {
        const response = await axios.get('dispense/' + id_dispensa + '/prodotti/' + id_nome+'/')
        return response
    }
    catch (e) {
        console.log(e)
    }
}

