// API endpoint for retrieving currency data
const API_URL = "https://api.exchangerate-api.com/v4/latest/";

// Get input elements
const fromCurrencyInput = document.getElementById("fromCurrency");
const toCurrencyInput = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");

// Get result element
const resultElement = document.getElementById("result");

// Retrieve currency data from API and store in array
let currencies = [];
fetch(API_URL)
  .then(response => response.json())
  .then(data => {
    currencies = Object.keys(data.rates);
    displayCurrencies(currencies);
  })
  .catch(error => console.error("Error retrieving currency data:", error));

// Display currency options in select elements
function displayCurrencies(currencies) {
  const selectElements = document.querySelectorAll("select");
  selectElements.forEach(selectElement => {
    currencies.forEach(currency => {
      const optionElement = document.createElement("option");
      optionElement.value = currency;
      optionElement.textContent = currency;
      selectElement.appendChild(optionElement);
    });
  });
}

// Convert currency based on input values
function convertCurrency() {
  const fromCurrency = fromCurrencyInput.value;
  const toCurrency = toCurrencyInput.value;
  const amount = amountInput.value;
  
  // Check that all input values are valid
  if (fromCurrency === "" || toCurrency === "" || amount === "") {
    resultElement.textContent = "Please enter all input values.";
    return;
  }
  
  // Perform currency conversion
  const rate = getConversionRate(fromCurrency, toCurrency);
  const convertedAmount = amount * rate;
  
  // Display converted amount
  const resultText = `${amount} ${fromCurrency} = ${convertedAmount} ${toCurrency}`;
  resultElement.textContent = resultText;
}

// Get conversion rate between two currencies
function getConversionRate(fromCurrency, toCurrency) {
  const apiEndpoint = `${API_URL}${fromCurrency}`;
  return fetch(apiEndpoint)
    .then(response => response.json())
    .then(data => data.rates[toCurrency])
    .catch(error => {
      console.error("Error retrieving conversion rate:", error);
      resultElement.textContent = "Error converting currency.";
      throw error;
    });
}

// Add event listeners to input elements
fromCurrencyInput.addEventListener("change", convertCurrency);
toCurrencyInput.addEventListener("change", convertCurrency);
amountInput.addEventListener("input", convertCurrency);
