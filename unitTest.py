import unittest
from fundCalculator import fund_calculator

class TestFund(unittest.TestCase):
    def test_payment_without_loan(self):
        result, customer_balance, customer_active_loan = fund_calculator(20,40,
                                                                         10,False)
        self.assertTrue(result)
        self.assertEqual(customer_balance,20)
        self.assertEqual(customer_active_loan, 10)

    def test_payment_with_loan(self):
        result, customer_balance, customer_active_loan = fund_calculator(20,10,
                                                                         11,True)
        self.assertTrue(result)
        self.assertEqual(customer_balance, 0)
        self.assertEqual(customer_active_loan, 1)

    def test_expense_greater_loan_and_balance(self):
        result = fund_calculator(20, 5,6, True)
        self.assertFalse(result)

    def test_expense_greater_balance(self):
        result = fund_calculator(20, 10,11, False)
        self.assertFalse(result)

    def test_expense_equal_balance(self):
        result, customer_balance, customer_active_loan = fund_calculator(20, 20,
                                                                         10, False)
        self.assertTrue(result)
        self.assertEqual(customer_balance, 0)
        self.assertEqual(customer_active_loan, 10)

    def test_expense_equal_balance_and_loan(self):
        result, customer_balance, customer_active_loan = fund_calculator(20, 9,
                                                                        11, True)
        self.assertTrue(result)
        self.assertEqual(customer_balance, 0)
        self.assertEqual(customer_active_loan, 0)

