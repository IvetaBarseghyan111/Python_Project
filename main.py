class MyBudget:
    def __init__(self, first_name, last_name, balance, active_loan):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.active_loan = active_loan
        self.expense = float(input("Please enter expense value "))

    def payment(self):
        if self.balance - self.expense >= 0:
            print("Payment successfully done from balance")
        elif self.balance < self.expense:
            user_answer = input("Do you want to cover remaining amount from active_loan")
            if user_answer == "yes":
                (self.balance - self.expense) - self.active_loan
                print("Payment successfully done from balance and active loan")
            else:
                print("Payment was cancelled")


customer1 = MyBudget("John", "Smith", 10,5)
customer1.payment()


