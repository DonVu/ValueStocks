import requests
import json

from stock_data import StockData

def stocks_api(stock_symbol):
    # The api fetching stock data
    url = 'https://financialmodelingprep.com/api/financials/'

    api_income_statement = requests.get(url + 'income-statement/' +
        stock_symbol)
    api_balance_statement = requests.get(url + 'balance-sheet-statement/' +
        stock_symbol)
    api_cash_statement = requests.get(url + 'cash-flow-statement/' +
        stock_symbol)

    income_statement = response_processing(api_income_statement)
    balance_statement = response_processing(api_balance_statement)
    cash_statement = response_processing(api_cash_statement)

    result = StockData(balance_statement, income_statement,
            cash_statement, stock_symbol)

    return result

def response_processing(api_response):
    if api_response.status_code == requests.codes.ok:
        stock_text = api_response.text
        edited_stock_text = stock_text.strip('<pre>')
        result = json.loads(edited_stock_text)

        return result
    else:
        print('Error finding stock or api source')

if __name__ == "__main__":
    example_data = stocks_api('GOOG')

    print(example_data.balance_sheet)
    print(example_data.income_statement)
    print(example_data.cash_flow_statement)
    print(example_data.stock_name)
