#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print ('Welcome to the tip calculator.')
inp_bill = input ('What was the total bill? £')
inp_tip = input ('What percentage tip would you like to give? ' )
inp_people = input ('How many people to split the bill? ')

#convert into relevant types
bill = float(inp_bill)
tip = float(inp_tip)
people = int (inp_people)

#put percent in the form 1.*
percent  = float(1 + tip/100)

each_person = float(bill/people)
total = (round(float(each_person * percent),2))
print(f'Each person should pay £{total} .')
