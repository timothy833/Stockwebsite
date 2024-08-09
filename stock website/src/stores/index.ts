import { defineStore } from 'pinia'
import { getApiList} from '../server'
import type { RootObject, Data, Info}  from './type'

export const useStore = defineStore({
  id:'counter',
    state: () => ({
      list: <RootObject>{},
      item:<Data>{}, 
      e:<Info>{}// 定義一個狀態，用於存儲從後端獲取的 JSON 數據
    }),
  actions: {
    async getList(){
      const result = await getApiList
      this.list = result
      // this.item = result
      
      // console.log(this.list)
      // return result.data
    }
  },
}
)
