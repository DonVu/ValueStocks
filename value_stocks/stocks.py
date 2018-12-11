from api import stocks_api
from interface import ask_stock_symbol
from heuristic import ai_heuristic

def main():
    stock_ticker = ask_stock_symbol()

    company_data = stocks_api(stock_ticker)
    
    stock_rating = ai_heuristic(company_data)

    print("\nThe company stock has a score of: %i (The higher the number, " % stock_rating +
            "the better the investment)" )

if __name__ == "__main__":
    main()
