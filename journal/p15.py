opened = open("userdata.csv", "w")
data = {}

while True:
    username = input("Enter username (EOF to end): ")

    if username == "EOF":
        break
    
    password = input("Enter password: ")
    data[username] = password

csv_string = "username,password"
for u, p in data.items():
    csv_string += "\n" + u + "," + p

opened.write(csv_string)
opened.flush()

userid = input("Search userid:")
print("Password: ", data[userid])
