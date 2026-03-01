import api from "@/utils/axios"
import { ref } from "vue"


export function useFetch() {

    const data = ref([])
    const loading = ref(false)
    const err = ref(null)

    const getData = async (url) => {
        loading.value = true
        try {
            const response = await api.get(url)
            data.value = response.data
        } catch (error) {
            err.value = error.response || error
        } finally {
            loading.value = false
        }
    }

    return { getData, data, loading, err }
}
