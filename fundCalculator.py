def fund_calculator (customer_expense,customer_balance,customer_active_loan,include_loan=False):
    if customer_expense <= customer_balance:
        customer_balance -= customer_expense
        return True, customer_balance, customer_active_loan
    elif include_loan and customer_expense <= (customer_balance + customer_active_loan):
        customer_active_loan = customer_active_loan - (customer_expense - customer_balance)
        customer_balance = 0
        return True, customer_balance, customer_active_loan
    else:
        return False
