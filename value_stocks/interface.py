def ask_stock_symbol():
    # Display user prompt and ask for stock symbol
    stock_ticker = raw_input("Enter the stock ticker symbol for the company: ")
    print
    stock_symbol = stock_ticker.upper()
    return stock_symbol

if __name__ == "__main__":
    ask_stock_symbol()
