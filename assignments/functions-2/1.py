def needlessly_recursive_prime_factors(num):
    p_factor = get_prime_factor(num)
    if p_factor:
        return [p_factor, *needlessly_recursive_prime_factors(num // p_factor)]
    else:
        return [num]


def get_prime_factor(num):
    for x in range(2, num):
        if num % x == 0 and is_prime(x):
            return x


def is_prime(num):
    if num < 2:
        return False

    return len([0 for x in range(2, num, 1) if num % x == 0]) == 0


print(needlessly_recursive_prime_factors(int(input("Enter number: "))))
