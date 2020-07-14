# Write your code here


print("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

print("Write how many cups of coffee you will need: ")
cups_of_coffee = 300
water = cups_of_coffee * 200
milk = cups_of_coffee * 50
coffee_beans = cups_of_coffee * 15

print("For " + str(cups_of_coffee) + " cups of coffee you will need: ")
print((str(water) + " ml of water"))
print((str(milk) + " ml of milk"))
print((str(coffee_beans) + " g of coffee beans"))

print("Write how many ml of water the coffee machine has:")
water_machine_has = abs(int(input()))
print("Write how many ml of milk the coffee machine has:")
milk_has = abs(int(input()))
print("Write how many grams of coffee beans the coffee machine has:")
coffee_has = abs(int(input()))
print("Write how many cups of coffee you will need:")
cups_needed_m = int(input())

if cups_needed_m == 0 and water_machine_has == 0 and milk_has == 0 and coffee_has == 0:
    print("Yes, I can make that amount of coffee")
elif 0 in (water_machine_has, milk_has, coffee_has):
    print("No, I can make only 0 cups of coffee")
elif ((water_machine_has // 200) == cups_needed_m) and ((milk_has // 50) == cups_needed_m) and ((coffee_has // 15) == cups_needed_m):
    print("Yes, I can make that amount of coffee")
elif ((water_machine_has // 200) < cups_needed_m) or ((milk_has // 50) < cups_needed_m) or ((coffee_has // 15) < cups_needed_m):
    max_cups = min((water_machine_has // 200), (milk_has // 50), (coffee_has // 15))
    print("No, I can make only " + str(max_cups) + "cups of coffee")
elif ((water_machine_has // 200) > cups_needed_m) and ((milk_has // 50) > cups_needed_m) and ((coffee_has // 15) > cups_needed_m):
    additional_cups = (min((water_machine_has // 200), (milk_has // 50), (coffee_has // 15)) - cups_needed_m)
    print("Yes, I can make that amount of coffee (and even" + str(additional_cups) + "more than that)")


