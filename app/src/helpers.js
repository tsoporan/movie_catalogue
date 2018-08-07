/*
 * Helpers
 */

import moment from "moment";

/**
 * Given an error response determine the error
 * message or fallback to a default.
 * @params {object} err
 * @returns {string} Error mesage
 */
const extractError = err => {
  let error = "Could not reach the server.";

  if (err.response) {
    error = err.response.data.error;
  } else if (error.request) {
    error = "No response.";
  }

  return error;
};

/**
 * Picks a "random" color from given colors
 * @params {array} colors
 * @returns {string}
 */
const pickColor = (
  colors = ["red", "orange", "purple", "green", "teal", "blue"]
) => {
  return colors[Math.floor(Math.random() * colors.length)];
};

/**
 * Returns a "random" ID, would use UUID normally
 * @returns {string}
 */
const randomId = (length = 5) => {
  return btoa(Math.random()).substring(0, length);
};


/**
 * Given a timestamp (unix) turns into date
 * @params {string} timestamp
 * @returns {string|null}
 */
const tsToDate = (timestamp) => {
  if (timestamp) {
    return moment.unix(timestamp).utc().format("YYYY-MM-DD HH:MM");
  }

  return null;
};

export { extractError, pickColor, randomId, tsToDate };
