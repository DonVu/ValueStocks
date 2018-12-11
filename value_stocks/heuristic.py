import json

from api import stocks_api

def ai_heuristic(company):
    stock_rating = 0

    """ Balance sheet ratios """

    """ Working Capital """
    if (int(company.balance_sheet[company.stock_name]['Total current assets']['2017-09']) >
            int(company.balance_sheet[company.stock_name]['Total current liabilities']['2017-09'])):
        stock_rating += 10

        print("Working capital is sufficient to pay short term debt(+10)")
    else:
        stock_rating -= 10
        print("Working capital is negative. Not enough to pay short term debt(-10)")


    """ Debt to Equity ratio """
    debt_to_equity = (float(company.balance_sheet[company.stock_name]['Total liabilities']['2017-09']) /
        float(company.balance_sheet[company.stock_name]["Total stockholders' equity"]['2017-09']))
    if (debt_to_equity > 0.50):
        stock_rating += 10

        print("Debt to Equity is higher than 50%% at: %.2f%% (+10)" %(debt_to_equity))
    else:
        stock_rating -= 40
        print("Debt to Equity is below average of 50%(-40)")

    """ Return On Equity ratio """
    return_on_equity = (float(company.income_statement[company.stock_name]['Net income']['2017-09']) /
        float(company.balance_sheet[company.stock_name]["Total stockholders' equity"]['2017-09']))
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




