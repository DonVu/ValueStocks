from api import stocks_api
from interface import ask_stock_symbol

def main():
    stock_ticker = ask_stock_symbol()

    company_data = stocks_api(stock_ticker)

    print(company_data.balance_sheet)

if __name__ == "__main__":
    main()
