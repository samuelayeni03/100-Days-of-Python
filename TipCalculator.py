print('Welcome to the tip calculator.')

#inputs the bill...
bill = float(input("What was the total bill: $"))

#inputs the percentage of tip...
percent_tip = int(input('What percentage tip would you like to give? 10, 12 or 15: '))

#inputs the number of people....
people = int(input('How many people to split the bill: '))

#calculates the total tip....
tip = ((percent_tip / 100) * bill)

#calculate the total bill....
total_bill = bill + tip

#calculates how much each person should pay...
individual_bill = total_bill / people

print(f'Each person should pay ${round(individual_bill, 2)}')