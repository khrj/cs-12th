print("Simple interest:", float(input('Simple interest:\nEnter p: ')) * float(input('Enter r: ')) * float(input('Enter t: ')) / 100)
print("Compound interest:", ((p := float(input('Compound interest:\nEnter p: '))) * (1 + float(input('Enter r: '))/100) ** float(input('Enter t: '))) - p)
