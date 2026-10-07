#Student name: Ryan Melendez
#Course number: CMP 31
#Week number: 6
#Lab number: Assingment 6
#Assignment title: Assingment 6
#Date: 10/7

quantity_input = input("Enter the number of software units purchased: ")
quantity = int(quantity_input)

if quantity <=0:
    print("Error: The number of units purchased must be greater then zero.")
else:
    price_pre_unit = 99.00
    original_cost = quantity * price_pre_unit

    if quantity < 10:
        discount_rate = 0.00
        discount_percent = "0%"

    elif quantity <=19:
        discount_rate = 0.20
        discount_percent = "20%"
    elif quantity <=49:
        discount_rate = 0.30
        discoutn_percent = "30%"
    elif quantity <=99:
        discount_rate = 0.40
        discount_percent = "40%"
    else:
        discount_rate = 0.50
        discount_percent = "50%"

discount_amount = original_cost * discount_rate
final_cost = original_cost - discount_amount

print()
print("PURCHASE REPORT")
print("Number of units purchased: ", quantity)
print("Price per unit: $", price_pre_unit)
print("Original cost: $", original_cost)
print("Discount percentage:", discount_percent)
print("Discount amount: $", discount_amount)
print("Final purchase cost: $", final_cost)