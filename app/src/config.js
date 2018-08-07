/*
 * Config
 */

import axios from "axios";

const API_URL = process.env.API_URL || "http://localhost:5000";

const ENDPOINTS = {
  movies: `${API_URL}/movies`,
  genres: `${API_URL}/genres`,
  actors: `${API_URL}/actors`
};

// Axios defaults
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

export { axios, ENDPOINTS };
