class StockData(object):
    """This class is used to hold the financial statements data for 
    for the company.

    Attributes:
        balance_sheet: dictionary containing the company balance sheet data.
        income_statement: dictionary containing the company income
                          statement data.
        cash_flow_statement: dictionary containing the company cash
                             flow statement.
    """
    def __init__(self, balance_sheet, income_statement,
            cash_flow_statement):
        """Inits StockData with financial data passed in"""
        self._balance_sheet = balance_sheet
        self._income_statement = income_statement
        self._cash_flow_statement = cash_flow_statement

    @property
    def balance_sheet(self):
        """Returns the balance sheet dictionary.
        
        Returns:
            a dictionary of dictionaries containing the data for
            each relevant balance sheet section.
        """
        return self._balance_sheet

    @balance_sheet.setter
    def balance_sheet(self, data):
        """Sets the object's balance sheet dict as data."""
        self._balance_sheet = data
 
    @property
    def income_statement(self):
        """Returns the income statement dictionary.
        
        Returns:
            a dictionary of dictionaries containing the data for
            each relevant income statement section.
        """
        return self._income_statement

    @income_statement.setter
    def income_statement(self, data):
        """Sets the object's income statement dict as data."""
        self._income_statement = data

    @property
    def cash_flow_statement(self):
        """Returns the cash flow statement dictionary.
        
        Returns:
            a dictionary of dictionaries containing the data for
            each relevant cash flow statement section.
        """
        return self._cash_flow_statement

    @cash_flow_statement.setter
    def cash_flow_statement(self, data):
        """Sets the object's cash flow statement dict as data."""
        self._cash_flow_statement = data

if __name__ == "__main__":
    example = StockData({'balance sheet' : 'test1'},
            {'income statement' : 'test2'},
            {'cash flow statement' : 'test3'})
    
    print(example.balance_sheet)
    print(example.income_statement)
    print(example.cash_flow_statement)

    example.balance_sheet = {'balance new' : 'new1'}
    example.income_statement = {'income new' : 'new2'}
    example.cash_flow_statement = {'cash new' : 'new3'}

    print(example.balance_sheet)
    print(example.income_statement)
    print(example.cash_flow_statement)
