#2) #რა არის Debugging და რატომ გამოიწვევს კოდი error-ს

##ჩვენ debugging-ს ვიყენებთ იმისთვის, რომ გავიგოთ:

#რატომ არ მუშაობს კოდი

#სად დავუშვით შეცდომა

#როგორ გამოვასწოროთ ეს შეცდომა
 
# print(my_name)
# my_name = "Your name
#ცვლადი my_name ჯერ არ არის შექმნილი, მაგრამ მის დაბეჭდვას ვცდილობთ → NameError

#ტექსტს აკლია დახურვის ბრჭყალი (") → SyntaxError

#3)
a = 10      
b = 2.5     

print(a + b)

#4)
x = 8
y = 4

print(x + y)  
print(x - y)  
print(x * y)  
print(x / y) 



#5)
age = 25
print(age + 5)



#6)
#კონკადინაცია ნიშნავს ტექსტების ერთმანეთთან შეერთებას + ოპერატორით.
name = "Giorgi"
surname = "Javakhishvili"
age = 15
city = "Tbilisi"

print("My name is " + name + " " + surname + ", I am " + str(age) + " years old and I live in " + city)


#7) 
#total = 100
#print(totl)
#ცვლადი totl არ არსებობს — სწორი სახელია total ამიტომ ერორს გამოიტანს



#8)
total = 120
people = 4

print(total / people)


#9)
price = 80
discount = 0.5

final_price = price - (price * discount)
print(final_price)



#10)
number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
