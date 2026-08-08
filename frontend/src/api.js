import axios from "axios";

const api = axios.create({

  baseURL: "http://a0ec389077d564fbbb0b76d766d10d00-1943124930.ap-south-1.elb.amazonaws.com:8000",

});

export default api;