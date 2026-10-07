#Student name: Ryan Melendez
#Course number: CMP 31
#Week number: 6
#Lab number: Assingment 6
#Assignment title: Assingment 6
#Date: 10/7

print("Choose a package:A,B,or C")
package = input("Enter package letter: ")
minutes = int(input("Enter number of minutes user: "))

if package == "A":
    base_charge = 39.99
    if minutes > 450:
        extra_minutes = minutes - 450
        total_bill = base_charge + (extra_minutes * 0.45)

    else:
        total_bill = base_charge
        print("Total Monthly Bill:$")
        print(total_bill)

elif package == "B":
    base_charge = 59.99
    if minutes > 900:
        extra_minutes = minutes - 900
        total_bill = base_charge + (extra_minutes * 0.40)
    else:
        total_bill = base_charge
        print("Total Monthly Bill: $")
        print(total_bill)
   
elif package == "C":
    total_bill == "C"
    total_bill = 69.99
    print("Total Monthly Bill: $")
    print(total_bill)

else:
    print("Invalid package selection.")