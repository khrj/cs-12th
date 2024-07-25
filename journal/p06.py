number_strings = input("Enter numbers separated by spaces: ").split(" ")
numbers = []

for number in number_strings:
    numbers.append(int(number))

positive = []
negative = []
prime = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)

    is_prime = True if number >= 2 else False
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break
    
    if is_prime:
        prime.append(number)

positive_avg = sum(positive) / len(positive)
right = int(input("Enter right shift amount: "))
right_shifted = numbers[-right:] + numbers[:-right]

negative.sort()    

print("Average:", positive_avg)
print("Right shifted:", right_shifted)

try:
    print("Highest and lowest negative:", negative[-1], negative[0])
except:
    print("No negative numbers")

print("Prime: ", prime)
