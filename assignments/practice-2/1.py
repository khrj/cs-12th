print((s := input("Enter string: "))[(amt := int(input("Amount: "))):] + s[:amt], s[-amt:] + s[:-amt]) 
