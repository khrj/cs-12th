ONE_CM_IS_X_INCHES = 0.393701
h = float(input("what's your height in cm?: "))
inches = h * ONE_CM_IS_X_INCHES
feet = inches // 12
inches_without_feet = inches % 12
print(f"Your height is: {feet}ft {inches_without_feet}in")