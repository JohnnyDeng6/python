#Johhny Deng
#ASB Friday night pizza party code
#10/05/22

pizza= ['veggie', 'meat', 'hawaiian', 'cheese']
drinks = ['water', 'coke', 'cranberry', 'fanta', 'sprite']
price = 0

print("Welcome to ASB Pizza Party. Here is our menu\n DRINKS")
c = 0
for a in drinks:
  if c == 0:
    print(a + " - Free")
    c = 1
  else:
    print(a + " - $0.75")
print(" PIZZA")
for a in pizza:
  print(a + " - $1.99")

YesOrNo = input("would you like a drink (yes/no)? ").lower().split()[0].strip("!?.,")
if YesOrNo == "yes":
  item = input("What drink would you like? ").lower().split()[0].strip(" !?.,")
  if item in drinks:
      if item != "water":
          price += 0.75
      amount = float(input("how many? "))
      price = price * amount
      print("Got it,", amount, item + "(s)")
  elif item not in drinks:
      print("Sorry we do not sell that drink")
elif YesOrNo == "no":
    print('ok')
else:
    print("Sorry, I didn't get that")




YesOrNo = input("would you like a pizza (yes/no)? ").lower().split()[0].strip(" !?.,")
if YesOrNo == "yes":
  item = input("What pizza would you like? ").lower()
  if item in pizza:
      amount = float(input("how many? "))
      price += (1.99 * amount)
      print("Got it,", amount, item + "(s) pizza")
  elif item not in pizza:
      print("Sorry we do not sell that pizza")
elif YesOrNo == "no":
    print('ok')
else:
    print("Sorry, I didn't get that")
    

price *= 1.05

print("That would be $ {price:.2f}".format(price = price))
