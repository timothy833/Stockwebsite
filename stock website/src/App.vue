<template>
  <div class = "d-flex">
    
        <input class = "form-control me-2" type = "search" placeholder = "請輸入股票名稱" aria-label = "Search" v-model="stockData1" />
        <button class = "btn btn-outline-success" type = "submit" @click="toPage('stockindex', stockData1)" > Search </button>
  </div>
  <div>
    <button  class = "fs-3" type = "submit"  @click="home('/')" > 股票平台首頁 </button>
  <br>
  <hr>
  <br>
  <router-view/>
  </div>
</template>

<script setup lang="ts">
import { useStore } from '../src/stores'
import {useRouter} from 'vue-router'
import { onMounted } from 'vue'
import { ref } from 'vue';

const store = useStore()

const router = useRouter()


const stockData1 = ref("");

// const stockData = ref({});

onMounted(
  async ()=>{
    await store.getList()
    // stockData.value = store.list.data
  }
)


const home = (url:string) => {
  router.push(url)
}


const toPage = (stockindex : string , query : string) => {
  router.push({
    name: stockindex,
    query: {search: query }
  })
}

</script>

<style>

</style>
