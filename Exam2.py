import random

def change_back_func(Amount_back, denomination):
    count = 0
    while Amount_back >= denomination:
        count+=1
        Amount_back -= denomination
        print(f'count is {count} of {denomination}')
    return (count)


total_dollar = random.randint(0, 101)

print('the total dollar amount is $', end=' ')
print(total_dollar)


total_cent = random.uniform(0, 1)

print('the total change is $', end=' ')
format = '{0:.2f}'.format(total_cent)
print(format)

Total_Amount = total_dollar + total_cent
format = '{0:.2f}'.format(Total_Amount)
print('the total amount is $',format)

Payment = round(random.uniform(Total_Amount, Total_Amount+100),2)
format = '{0:.2f}'.format(Payment)
print('the amount payed is $',format)

Amount_back = Payment - Total_Amount
Check_amount_back = Amount_back
format = '{0:.2f}'.format(Amount_back)
print('the change given back is $',format)

print('Now we give back change')

Denominations = [20,10,5,1,.25,.1,.05,.01]
change = []
for index in range (len(Denominations)):
    print(f'for index {index}, Denominations is {Denominations[index]}.')


    change.append( change_back_func (Amount_back, Denominations[index]))
    Amount_back = Amount_back - change[index] * Denominations[index]


print('We are done with the for loop')
Total_Change = 0
for index in range (len(Denominations)):
    print(f'for demoniation {Denominations[index]}, Total was{change[index] * Denominations[index]}.')
    Total_Change = Total_Change + change[index] * Denominations[index]
print(f'We ended up giving back {Total_Change}.')
print('We wanted to give back', Check_amount_back)
