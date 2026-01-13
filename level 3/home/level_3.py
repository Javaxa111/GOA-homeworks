#1) გამოასწორეთ ქვემოთ მოცემული კოდი რომ terminal - ში დაიბეჭდოს შედეგად 8 error - ის მაგივრად

a = 5
b = 3
sum = 5 + b
print(sum)


#2) მოიძიეთ ინფორმაცია converter - ების შესახებ პითონში და გააკეთეთ თითოეულზე 2-2 მაგალითი
#Converter-ები არის ფუნქციები, რომლებიც მონაცემებს ერთი ტიპიდან (მაგ. string) მეორე ტიპად (მაგ. int) გარდაქმნიან.

#1. int() — გარდაქმნის მნიშვნელობას მთელ რიცხვად
num_str = "25"
num_int = int(num_str)    
print(num_int + 5) 

num_str = "31"
num_int = int(num_str)
print(num_int + 13)

#2.str() — გარდაქმნის მნიშვნელობას სტრიქონად
num = 100
text = str(num)
print("რიცხვი არის: " + text)


num = 1234
text = str(num)
print("this number is :" + text)


#3. float() — გარდაქმნის მნიშვნელობას ათწილადად

num_str = "3.14"
num_float = float(num_str)
print(num_float + 1)      


num_str = "123"
num_float = float(num_str)
print(num_float + 12)


#მომხმარებელს შემოატანინეთ ორი ათწილადი რიცხვი დააჯამეთ ისინი და გამოიტანეთ საბოლოო შედეგი ეკრანზ

num1 = float(input("შეიყვანეთ თვენი რიცხვი : "))
num2 = float(input("შეიყვანეთ მეორე ათწილადი რიცხვი :"))

result = num1 + num2
print("რიცხვების ჯამია : " , result)



#მომხმარებელს შემოატანინეთ ორი მთელი რიცხვი, თქვენი დავალებაა რომ შეამოწმოთ თუ ორივე რიცხვი % 2 მიღებული ნაშთი უდრის 0 - ს ანუ თუ რიცხვი ლუწია მაშინ გამოიტანეთ ამ ორი რიცხვის ჯამი, სხვა შემთხვევაში კი დაბეჭდეთ რომ 'The given numbers are not even so they will not be summed', (შეგიძლიათ მოიძიოთ ინფორაციაც)

num1 = int(input("შეიყვანეთ მთელი რიცხვი :"))
num2 = int(input("შეიყვანეთ მთელი რიცხვი :"))

if num1 % 2 == 0 and num2 % 2 == 0:
    result = num1 + num2
    print("ორივე რიცხვი ლუწია მათი ჯამია:" , result)
else :
    print("The given numbers are not even so they will not be summed")




#მომხმარებელს შემოატანინეთ თავისი სახელი გვარი ასაკი ქალაქი ქვეყანა, და გამოიტანეთ შედეგი მსგავსად
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
country = input("Enter your country: ")


print("Your name is:", name)
print("Your surname is:", surname)
print("Your age is:", age)
print("You live in:", city)
print("The country you live in is:", country)


#მომხმარებელს შემოატანინეთ ორი რიცხვი, თქვენი დავალებაა რომ ამ ორ რიცხვზე გამოიყენოთ ყველა მათემატიკური ოპერაცია როგორიცაა -+/*

num1 = int(input("ჩაწერეთ რიცხვი :"))
num2 = int(input("ჩაწერეთ მეორე რიცხვი :"))

jami = num1 + num2
sxvaoba = num1 - num2
namravli = num1 * num2
gayofa = num1 / num2

print(jami , sxvaoba , namravli , gayofa)


#შექმენით ერთი ცვლადი მასში შეინახეთ თქვენი სახელი, მომხმარებელს შემოატანინეთ რაიმე სახელი, შეამოწმეთ თუ მომხმარებლის მიერ შემოტანილი სახელი უდრის თქვენს ცვლადში შენახულ სახელს დაბეჭდეთ 'We have the same name' სხვა შემთხვევაში 'Our names do not match'

name = "Giorgi"
name2 =input("შეიყვანე შენი სახელი :")


if name2 == name :
    print("We have the same name")
else:
    print("Our names do not match")




#კონკადინაცია ნიშნავს სტრიქონების შეერთებას ერთმანეთთან. ანუ როცა ორ ან მეტ ტექსტს ვაერთებთ ერთ მთლიან ტექსტად. 

print('45' + "45")
#ეს გამოიტანს 4545 რადგან ორივე სტრინგის ფორიმისაა და მათემატიკურ შესრულებას ვერ გააკეთებს 




#მომხმარებელს შემოატნინეთ რაიმე რიცხვი, შეამოწმეთ თუ რიცხვის % 2 ნაშთი უდრის 0 - ს გამოიტანეთ რომ 'The number is even' სხვა შემთხვევაში კი 'The number is odd'


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")






#comparation operator - სექციის გავლის შემდეგ  გააკეთეთ რამოდენიმე მაგალითი

a = 5
b = 10

print(a == b)  # False, 5 არ უდრის 10-ს
print(a != b)  # True, 5 არ უდრის 10-ს
print(a < b)   # True, 5 ნაკლებია 10-ზე
print(a > b)   # False, 5 არ არის დიდი 10-ზე
