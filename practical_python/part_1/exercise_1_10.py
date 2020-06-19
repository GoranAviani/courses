"""
Exercise 1.10: Making a table
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

        print('{}  {}  {}' .format(month_no, total_paid, principal))
    print("Total paid", total_paid)
    print("Months", month_no)

if __name__ == '__main__':
    main()