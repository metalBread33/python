
#Get details of loan
moneyOwed = float (input("How much do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate of the loan?\n"))
payment = float(input('How much will you pay off each month in dollars? \n'))
months = int(input ("How many months do you want to see the results for?\n"))

monthlyRate = apr/100/12

for i in range(months):
    #calculate first months intrest
    interestPaid = moneyOwed*monthlyRate

    #Add intrest
    moneyOwed = moneyOwed + interestPaid
    if(moneyOwed - payment < 0):
        print('The last payment is', moneyOwed)
        print('You paid of the loan in', i+1, 'months')
        break

    #Make payment
    moneyOwed = moneyOwed - payment

    print('Paid', payment, 'of which', interestPaid, 'was intrest', end=' ')
    print('Now I owe', moneyOwed)