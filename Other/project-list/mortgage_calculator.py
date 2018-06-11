#Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
#Also figure out how long it will take the user to pay back the loan.
#For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).


#PMT function for financial calculation
def pmt_function(rate):
    return (rate/100/12)


def main():
    months = int(input("How many months is your mortgage:  "))
    rate = float(input("What is the rate of your mortgage in %: "))
    loan = float(input("How much is your loan: "))

    pmtRate = pmt_function(rate)

    #mortgage calculation
    monthlyPayment = loan * (pmtRate * (1 + pmtRate) ** months) / ((1+pmtRate) ** months -1)
    print("Your loan {} with interest rate of {}% ower the time period of {} "
          "months means you have to repay {} per month".format(loan, rate, months, round(monthlyPayment,2)))


if __name__ == "__main__":
    main()
