def sumPdivisors(num):
    return sum([x for x in range(1, num) if num % x == 0])

def are_amicable(one, two):
    return sumPdivisors(one) == two and sumPdivisors(two) == one

print(are_amicable(int(input("Enter number 1: ")), int(input("Enter number 2: "))))
