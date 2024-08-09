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
    async getList() {
      try{
        const result = await getApiList(); // 调用getApiList获取数据
        this.list = result  // 将获取的数据赋值给state中的list
      }
      catch (error) {
        console.error("Error in getList action:", error);
      }
      // this.item = result
      
      // console.log(this.list)
      // return result.data
    }
  },
}
)
