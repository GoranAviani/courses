"""
Exercise 1.8: Extra payments

Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

When you run the new program, it should report a total payment of 929,965.62 over 342 months.
"""




def main():
    principal = 500000.0
    rate = 0.05

    total_paid = 0.0
    month_no = 0

    while principal > 0:
        month_no += 1
        payment = 2684.11
        if month_no < 13:
            payment = 3684.11
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

    print('Total paid {}, month number {}' .format(total_paid, month_no))

if __name__ == '__main__':
    main()