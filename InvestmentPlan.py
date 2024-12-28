print("ENTER INVESTMENT AMOUNT")
investmentAmount = float(input())

print("ENTER MONTHLY CONTRIBUTION")
monthlyContribution = float(input())

print("ENTER DURATION IN YEARS")
lengthOfTime = int(input())

print("SELECT A NUMBER TO SELECT")
amountPerFrequency =[365, 12, 1]
print("""
0 = daily.
1 = monthly.
2 = yearly.
""")
compoundFrequency = int(input())
amountPerFrequencyChoosen = amountPerFrequency[compoundFrequency]

print("ENTER PREFERED INTEREST RATE")
interestRate = float(input())

totalAmount = investmentAmount
for year in range(lengthOfTime):

    totalAmount = totalAmount + totalAmount * interestRate / amountPerFrequencyChoosen
    totalAmount = totalAmount * monthlyContribution * 12

print(f"TOTAL INVESTMENT AMOUNT FOR {interestRate}% is ${totalAmount:.2f}")