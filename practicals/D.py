# Create file 
open("story.txt", "a+").close()

def count_words_with_vowel():
    with open("story.txt", "r") as f:
        text = f.read()
        words = text.replace("\n", " ").split(" ")
        count = 0

        for word in words:
            if len(word) > 0 and word[0] in "aeiou":
                count += 1

        print(f"Number of words starting with any vowel: {count}")


def count_lines_ending_a():
    with open("story.txt", "r") as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if line.strip()[-1] == "a":
                count += 1

        print(f"Number of lines ending with the letter 'a': {count}")


def count_digits():
    with open("story.txt", "r") as f:
        text = f.read()
        count = 0

        for char in text:
            if char.isdigit():
                count += 1

        print(f"Number of digits: {count}")


while True:
    print("What would you like to do?")
    print("1. Count the number of words starting with any vowel")
    print("2. Count the number of lines ending with the letter A")
    print("3. Count the number of digits")
    print("4. Exit")

    choice = input("Enter choice: ")
    print()

    if choice == "1":
        count_words_with_vowel()
    elif choice == "2":
        count_lines_ending_a()
    elif choice == "3":
        count_digits()
    elif choice == "4":
        break
    else:
        print("Invalid choice")

    print()
