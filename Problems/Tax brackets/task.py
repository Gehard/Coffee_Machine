money = abs(int(input()))

if money <= 15527:
    percent = 0
    calculated_tax = round((percent / 100) * money)
    print(f"The tax for {money} is {percent}%. That is {calculated_tax} dollars!")
elif 15528 <= money <= 42707:
    percent = 15
    calculated_tax = round((percent / 100) * money)
    print(f"The tax for {money} is {percent}%. That is {calculated_tax} dollars!")
elif 42708 <= money <= 132406:
    percent = 25
    calculated_tax = round((percent / 100) * money)
    print(f"The tax for {money} is {percent}%. That is {calculated_tax} dollars!")
elif money >= 132407:
    percent = 28
    calculated_tax = round((percent / 100) * money)
    print(f"The tax for {money} is {percent}%. That is {calculated_tax} dollars!")
