import axios from 'axios';

axios.defaults.baseURL = 'http://192.168.1.233:8000/api/' //'http://localhost:8000/api/';

export { axios };