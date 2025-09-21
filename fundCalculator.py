def fund_calculator(self, customer_expense, include_loan=False):
    if customer_expense <= self._customer_balance:
        self._customer_balance -= customer_expense
        return True
    elif include_loan and customer_expense <= (self._customer_balance + self._customer_active_loan):
        self._customer_active_loan = self._customer_active_loan - (customer_expense - self._customer_balance)
        self._customer_balance = 0
        return True
    else:
        return False
