quantity = input("Welcome to The Loop Hole! \nToday's Manager's Special is Crunch Jelly: \nA traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries \nHow many would you like?")
quantity = float(quantity)

pay = input("How much would you like to pay for each donut?")
pay = float(pay)

print("ok, allow me to prepare your order.")
total = quantity * pay
tax = total*0.05
total = total + tax
print("After tax your total comes out to:")
print("$""{:.2f}".format(total))
