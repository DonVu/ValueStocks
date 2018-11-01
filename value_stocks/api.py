import requests

def stocks_api(stock_symbol):
    # The api fetching stock data
    url = 'https://financialmodelingprep.com/api/financials/income-statement/'

    api_response = requests.get(url + stock_symbol)
    
    if api_response.status_code == requests.codes.ok:
        # TODO(don): Remove the debugging print statement after testing function
        print(api_response.text)

if __name__ == "__main__":
    stocks_api('GOOG')
