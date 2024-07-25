string = ""

print("Enter a multiline string. Type EOF to finish")
while True:
    line = input()
    if line == "EOF":
        break
    else:
        string += line + "\n"

string = string.rstrip()

words_count = len(string.replace("\n", " ").split(" "))
lines_count = len(string.split("\n"))
characters_count = len(string)

digits, vowels, consonants = 0, 0, 0

for char in string:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1

india_count = 0
for word in string.replace("\n", " ").split(" "):
    if word.lower() == "india":
        india_count += 1

print("Words:", words_count, "Lines:", lines_count, "Characters:", characters_count)
print("Digits:", digits, "Vowels:", vowels, "Consonants:", consonants)
print("India appears", india_count, "times")
print(
    string.replace(
        "India",
        "New Delhi",
    )
)
