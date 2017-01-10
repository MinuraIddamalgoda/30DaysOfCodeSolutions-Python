mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = 12 * (tipPercent/100)
tax = 12 * (taxPercent/100)

totalCost = mealCost + tip + tax
# round(number, nDigits) is a function that rounds the first paramter, number, to the
# amount of digits specified by nDigits. So in this case, it will round the total cost of
# the meal to two digits. Be weary though that in python2 it rounds down at 2.675 to 2.7 whereas
# in python3 three it rounds up at 2.675 to 2.8
round(totalCost, 2)

print('The total meal cost is', totalCost, 'dollars.', sep=' ')
