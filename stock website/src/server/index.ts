import axios from 'axios'

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
  });


export const getApiList = async () => {
  try {
    const response = await api.get("/stock");  // 发起GET请求
    return response.data;  // 返回数据
  } catch (error) {
    console.error("Error fetching API list:", error);
    throw error;  // 抛出错误以便在调用处处理
  }
};



// export const getApiList = api
//     .get("/stock")
//     .then((res) => { return res.data })
//     .catch((error) => console.log(error));


// export const getApiList  = axios
    // .get("http://127.0.0.1:8080/stock")
    // .then((res) => {return res.data})
    //http://127.0.0.1:8080//tmp_stock/0050
    //then設定成功狀況 catch設定失敗狀況
    //return res.data 需要設定呼叫的回傳資料
    //console.log(response.data))只有印東西，沒有回傳
    // .catch((error) => console.log(error));