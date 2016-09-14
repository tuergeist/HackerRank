mealCost = float(input())
tipPercent = float(input())
taxPercent = float(input())

tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100

print("The total meal cost is %s dollars." % round(mealCost + tip + tax))