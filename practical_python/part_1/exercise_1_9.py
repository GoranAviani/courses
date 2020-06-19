"""
Exercise 1.9: Making an Extra Payment Calculator

Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

Make the program look at these variables and calculate the total paid appropriately.

How much will Dave pay if he pays an extra $1000/month for 4 years starting in year 5 of the mortgage?
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
            payment = payment + extra_payment_end_month
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

    print('Total paid {}, month number {}' .format(total_paid, month_no))

if __name__ == '__main__':
    main()