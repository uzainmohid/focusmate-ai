import axios from "axios";

// This should point to your deployed backend on Render
const API_URL = import.meta.env.VITE_API_URL;

export const api = axios.create({
  baseURL: API_URL,
});
