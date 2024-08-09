<template>
    <div class="box">
    
      <div style="color: red"   class="box-right"  >
        <table class="table" cellspacing="0" border="1"  v-if="stockName">
            <tr>
              <th colspan="7">股票名稱:{{stockName.name}}</th>
            </tr>
            <tr>
              <!-- 跨行置中colspan 數字是跨幾行 跨列置中rowspan       -->
              <th colspan="4">除息</th>
              <th colspan="3">填息</th>
            </tr>
            <tr>
                <th>發放年度</th>
                <th>發放形式(季配)</th>
                <th>交易日</th>
                <th>參考價</th>
                <th>日期</th>
                <th>花費天數</th>
                <th>發放股息日期</th>         
            </tr>
            <tr  v-for="item in stockName.info" >
              <td align="center">{{ item.dividend_payment.year }}</td>
              <td align="center">{{ item.dividend_payment.type }}</td>
              <td align="center">{{ item.XD.trade_date }}</td>
              <td align="center">{{ item.XD.reference_price }}</td>
              <td align="center">{{ item.XD.refill_finish_date }}</td>
              <td align="center">{{ item.XD.refill_cost_days }}</td>
              <td align="center">{{ item.XD.cash_dividend_payment }}</td>
            </tr>
        </table>
      </div>
    </div>
    </template>
    
    <script setup lang="ts">
    import { useStore } from '../stores'
    // import { onMounted } from 'vue'
    import { ref, computed } from 'vue'
    import { useRoute } from 'vue-router';

    const route = useRoute()
    const stockDataRef = ref('s' + (route.query.search || ''));
    const store = useStore()
    // const stockData = ref<any>({})
    

    // onMounted(
    //   async ()=>{
    //     await store.getList()
    //     // stockData.value = store.list.data
    //     console.log(store.list.data)
    //     console.log(1)
    //     // if (route.query.search) {
    //     //   stockDataRef.value = 's' + route.query.search;
    //     // } 

    //   }
    // )

    const stockName = computed(() => {
      if (route.query.search) {
          stockDataRef.value = 's' + route.query.search;
        } 
      const key = stockDataRef.value as keyof typeof store.list.data; // 类型断言
      console.log(store.list.data)
      return store.list.data[key] || '';
    });
   
  
    </script>
    
    <style lang="less">
    *{
      padding: 0;
      margin: 0;
    }
    .table{
      width: 100%;
      background: #212028;
      tr{
        th{
          padding: 5px;
          // 處理空白字符:影響表格內換行
          white-space: pre;
        }
        td{
          padding: 5px 10px;
          width:100%;
          white-space: normal;
        }
      }
    }
    html,
    body,
    #app{
      height: 100%;
    }
    
    .box{
      height: 100%;
      display: flex;
      &-left{
        width: 600px;
        
      }
      &-center{
        flex:1;
      }
      &-right{
        width: 600px;
      }
    }
    </style>
    