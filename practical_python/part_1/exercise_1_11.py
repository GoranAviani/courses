"""
Exercise 1.11: Bonus

While you’re at it, fix the program to correct for the overpayment that occurs in the last month.
"""

def main():
    principal = 500000.0
    rate = 0.05

    total_paid = 0.0
    month_no = 0

    extra_payment_start_month = 60
    extra_payment_end_month = 108
    extra_payment = 1000

    while principal > 0:
        month_no += 1
        payment = 2684.11
        if month_no > extra_payment_start_month and month_no < extra_payment_end_month:
            payment = payment + extra_payment
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        if principal < 0:
            principal = 0

        print('{}  {}  {}' .format(month_no, round(total_paid, 2), round(principal, 2)))
    print("Total paid", round(total_paid, 2))
    print("Months", month_no)

if __name__ == '__main__':
    main()