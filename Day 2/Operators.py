mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = 12 * (tipPercent/100)
tax = 12 * (taxPercent/100)

totalCost = round(mealCost + tip + tax)

print('The total meal cost is',totalCost,'dollars.', sep=' ')