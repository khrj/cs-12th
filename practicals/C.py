# Stack functions. These six (size, is_empty, push, pop, top, display) are
# mandatory to implement, even if they seem trivial or not useful otherwise.


def size(stk):
    return len(stk)


def is_empty(stk):
    if size(stk) == 0:
        return True
    else:
        return False


def push(stk, m):
    stk.append(m)


def pop(stk):
    if is_empty(stk):
        print("Stack underflow")
    else:
        return stk.pop()


def top(stk):
    if is_empty(stk):
        print("Stack underflow")
        return None
    else:
        return stk[-1]


def display(stk):
    print("Current elements in stack are: ")
    for i in range(len(stk)):
        print(stk[-i - 1])


stack = []

while True:
    print("What would you like to do?")
    print("1. Push element onto stack")
    print("2. Pop element off stack")
    print("3. Display stack")
    print("4. Peek at stack")
    print("5. Exit")

    choice = input("Enter choice: ")
    print()

    if choice == "1":
        element = input("Enter element to push: ")
        push(stack, element)
    elif choice == "2":
        element = pop(stack)
        if not element:
            print("Stack is empty.")
        else:
            print(f"Element is: {element}")
    elif choice == "3":
        display(stack)
    elif choice == "4":
        elm = top(stack)
        if elm:
            print(f"Element on top is: {element}")
    elif choice == "5":
        break
    else:
        print("Invalid choice")

    print()
