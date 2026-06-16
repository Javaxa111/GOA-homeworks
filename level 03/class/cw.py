# input – გამოიყენება მომხმარებლისგან ინფორმაციის მისაღებად
# output – გამოიყენება ინფორმაციის გამოსატანად (print)

name = input("Enter your name: ")
print(name)


# მომხმარებლის სახელი, გვარი და ასაკი

first_name = input("Enter your name: ")
last_name = input("Enter your surname: ")
age = input("Enter your age: ")

print(first_name, last_name, age)


# ასაკის შემოწმება

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a kid")


# 0-დან შეყვანილ რიცხვამდე დაბეჭდვა

num = int(input("Enter a number: "))

for i in range(0, num + 1):
    print(i)
