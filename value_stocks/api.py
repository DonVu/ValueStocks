import requests
import json

def stocks_api(stock_symbol):
    # The api fetching stock data
    url = 'https://financialmodelingprep.com/api/financials/income-statement/'

    api_response = requests.get(url + stock_symbol)
    
    if api_response.status_code == requests.codes.ok:
        # TODO(don): Remove the debugging print statement after testing function
        stock_text = api_response.text
        edited_stock_text = stock_text.strip('<pre>')
        example = json.loads(edited_stock_text)
        #print(example['GOOG']['Revenue']['2013-12'])

if __name__ == "__main__":
    stocks_api('GOOG')
