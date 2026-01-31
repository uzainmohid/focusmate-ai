import axios from "axios";

const API_URL = "https://focusmate-backend-a0ce.onrender.com";

export const api = axios.create({
  baseURL: API_URL,
});
