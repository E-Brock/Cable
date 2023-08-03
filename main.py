message = "Welcome to AI Cable"
print(message)
message = "Save money on cable length"
print(message)
name = input("Tell us your company name: ")
print(f"\nWelcome, {name}!")
feet = float(input("How much cable would you like to purchase?: "))
if feet>500:
  total_cost=feet*0.50
elif feet>250:
  total_cost=feet*0.70
elif feet>100:
  total_cost=feet*0.80
else:
  total_cost=feet*0.87
print("Total_cost of Fiber Cable : $", total_cost, "for",name, "to purchase",feet, "ft.")