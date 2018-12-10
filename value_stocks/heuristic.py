import json

from api import stocks_api

def ai_heuristic(company):
    stock_rating = 0

    """ Balance sheet ratios """

    """ Working Capital """
    if (company.balance_sheet[company.stock_name]['Total current assets']['2017-09'] >
            company.balance_sheet[company.stock_name]['Total current liabilities']['2017-09']):
        stock_rating += 10

        print("Working capital is sufficient to pay short term debt(+10)")
    else:
        stock_rating -= 10
        print("Working capital is negative. Not enough to pay short term debt(-10)")

    return stock_rating       

if __name__ == "__main__":
    example_company = stocks_api("AAPL")

    print(ai_heuristic(example_company))




