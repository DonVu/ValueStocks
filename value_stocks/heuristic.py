import json
from datetime import datetime

from api import stocks_api

def ai_heuristic(company):
    stock_rating = 0

    """ 
        To find the latest year, The keys for the dictionary
        are compared to each other for use in the ratios.
    """
    latest_date = '2013-09'
    for key in company.balance_sheet[company.stock_name]['Total current assets']:
        if datetime.strptime(latest_date, '%Y-%d') < datetime.strptime(key, '%Y-%d'):
            latest_date = key

    """ Balance sheet ratios """

    """ Working Capital """
    if (int(company.balance_sheet[company.stock_name]['Total current assets'][latest_date]) >
            int(company.balance_sheet[company.stock_name]['Total current liabilities'][latest_date])):
        stock_rating += 10

        print("Working capital is sufficient to pay short term debt(+10)")
    else:
        stock_rating -= 10
        print("Working capital is negative. Not enough to pay short term debt(-10)")


    """ Debt to Equity ratio """
    debt_to_equity = (float(company.balance_sheet[company.stock_name]['Total liabilities'][latest_date]) /
        float(company.balance_sheet[company.stock_name]["Total stockholders' equity"][latest_date]))
    if (debt_to_equity > 0.50):
        stock_rating += 10

        print("Debt to Equity is higher than 50%% at: %.2f%% (+10)" %(debt_to_equity))
    else:
        stock_rating -= 40
        print("Debt to Equity is below average of 50%(-40)")

    """ Return On Equity ratio """
    return_on_equity = (float(company.income_statement[company.stock_name]['Net income'][latest_date]) /
        float(company.balance_sheet[company.stock_name]["Total stockholders' equity"][latest_date]))
    if (return_on_equity > 0.10):
        stock_rating += 30

        print("Return on equity is healthy at: %.2f (+30)" %(return_on_equity))
    else:
        stock_rating -= 20
        print("Return on equity is below average(-20)")

    return stock_rating       

if __name__ == "__main__":
    example_company = stocks_api("AAPL")

    print(ai_heuristic(example_company))




