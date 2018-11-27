import requests
import json

def stocks_api(stock_symbol):
    # The api fetching stock data
    url = 'https://financialmodelingprep.com/api/financials/'

    api_income_statement = requests.get(url + 'income-statement/' +
        stock_symbol)
    api_balance_statement = requests.get(url + 'balance-sheet-statement/' +
        stock_symbol)
    api_cash_statement = requests.get(url + 'cash-flow-statement/' +
        stock_symbol)  
    

def response_processing(api_response):
    if api_response.status_code == requests.codes.ok:
        stock_text = api_response.text
        edited_stock_text = stock_text.strip('<pre>')
        result = json.loads(edited_stock_text)

        return result
    else:
        print('Error finding stock or api source')

if __name__ == "__main__":
    stocks_api('GOOG')
