print("Welcome to Mal's Pizza Delivery")

# ask for input
# convert input to uppercase
size = (input("What size pizza do you want? S, M or L: ")).upper()
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra chees on your pizza? Y or N: ").upper()

# initialize total
total_cost = 0

# begin with statements for size
# nest add+pepperoni to each if
if size == "S":
    total_cost += 15
    if add_pepperoni == "Y":
        total_cost += 2
elif size == "M":
    total_cost += 20
    if add_pepperoni == "Y":
        total_cost += 3
elif size == "L":
    total_cost += 25
    if add_pepperoni == "Y":
        total_cost += 3
# add iff statement separately for extra_cheese
if extra_cheese == "Y":
    total_cost += 1

# print out total bill
print(f"Your final bill is ${total_cost}.")
