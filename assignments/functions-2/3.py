def sumPdivisors(num):
    return sum([x for x in range(1, num) if num % x == 0])


print(sumPdivisors(int(input("Enter number: "))))
