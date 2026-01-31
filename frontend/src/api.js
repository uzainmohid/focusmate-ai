import axios from "axios";

const API_URL = "https://focusmate-ai-s6n8.onrender.com";

export const api = axios.create({
  baseURL: API_URL,
});
