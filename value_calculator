print("Earned amount:\nBubblegum: $202\nToffee: $118\nIce cream: $2250\nMilk chocolate: $1680\nDoughnut: $1075\nPancake: $80")

monthEarned = [202, 118, 2250, 1680, 1075, 80]


def totalIncome():
    counter = 0
    amount = 0
    while counter < len(monthEarned):
        amount += monthEarned[counter]
        counter += 1
    return amount


print()
print("Income: " + str(totalIncome()))
amount = totalIncome()

staffExpenses = int(input("Staff expenses:"))
otherExpenses = int(input("Other expenses:"))

print(f"Net Income:", {amount - staffExpenses - otherExpenses})
