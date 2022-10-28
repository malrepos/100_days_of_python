even_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_sum += number

print(f"The sum of all evens between 1 and 100 is {even_sum}.")
