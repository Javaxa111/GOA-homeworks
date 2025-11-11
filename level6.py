#1)მომხმარებელს შემოატანინეთ password - ი, სულ ექნება 3 მცდელობა, თქვენი დავალებაა რომ გამოიყენოთ while loop - ი და იქმადე მოსთხოვოთ მომხმარებელს პაროლის შემოტანა სანამ ის არ გამოიცნობს მას ასევე დაიმახსოვრეთ მდელობების რაოდენობაც,
# თუ მცდელობების რაოდენობა == 3 მაშინ გამოიტანეთ message - You have reached the maximum number of attempts


correct_password = "11111111"   # სწორი პაროლი
attempts = 0                     # მცდელობების რაოდენობის საწყისი 

while attempts < 3:              # მანამდე იმუშავებს სანამ მცდელობა ნაკლებია 3-ზე
    password = input("Enter password: ")  # მომხმარებლისგან ვითხოვთ პაროლს
    if password == correct_password:      # თუ პაროლი სწორია
        print("Access granted ")                             
    else:
        attempts += 1                     # მცდელობების რაოდენობა +1
        print("Incorrect password")
        print("Attempts left:", 3 - attempts)

if attempts == 3:
    print("You have reached the maximum number of attempts")

#2) გადახედეთ მოცემულ კოდს და თქვენით დაფიქრდით თუ რას გამოიტანს ის
print(True and False and 5 > 9 and 90 * 30 > 1089 or False and 'Nino' != '' or False or True and 56 * 2 > 90)   


#3)კომენტარების სახით ახსენით თუ რა არის მასივი, შეგვიძლია თუ არა მასში ნებიმიერი მონაცემთა ტიპის შენახვა მაგალითად str, int, float, boolean და ა.შ.
# მასივი ან სია (list) არის მონაცემთა სტრუქტურა,
# რომელიც შეიცავს ელემენტების კოლექციას ერთ ცვლადში.

# შეგვიძლია მასივში შევინახოთ ნებისმიერი ტიპის მონაცემი:
# string, int, float, boolean და სხვა.


#4)შექმენით მასივი სადაც შეინახავთ თქვენი ოჯახის წევრების სახელებს, თქვენი დავალებაა რომ მოცემულ მასივს for loop - ის გამოყენებით გადაუაროთ და გამოიტანოთ თითოეული ელემენტი
family = ["Giorgi", "Nino", "Maka", "Mariam" , "Gela"]
for member in family:
    print(member)

#5)შექმენით მასივი სადაც შეინახავთ რიცხვებს თქვენი დავალებაა რომ გამოიტანოთ ამ მასვში არსებული ყველა რიცხვის ჯამი
numbers = [5, 10, 15, 20, 25]
total = 0

for num in numbers:
    total += num  

print("Total sum:", total)  


#6)# Indexing ნიშნავს ელემენტზე წვდომას მისი ინდექსით (ადგილმდებარეობით) კი შეგვიძლია გამოვიყენოთ სტრინგებზეც.


#7)კომენტარების სახით ახსენით თუ რატომ არის კარგი პრაქტიკა indexing - ის გამოყენება, რაში შეიძლება რომ გამოვიყენოთ ჩვენ ის
# Indexing გვეხმარება კონკრეტულ ელემენტზე წვდომაში.
# მაგალითად, თუ გვინდა სახელის პირველი ასო ან სიის ბოლო ელემენტი.

#8)თქვენით გააკეთეთ indexing - ზე 5-5 მაგალითი და კარგად გაიაზრეთ
text = "Python"
print(text[0])   
print(text[1])   
print(text[-1]) 
print(text[2:5])
print(text[:3])  

#9)შექმენით მასივი სადაც შეინახავთ ხილის სახელებს, თქვენი დავალებაა, რომ გამოიტანოთ ყოველი მეორე ელემენტი, მოიძიეთ ინფორმაცია slicing - ის შესახებ პითონში
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

print(fruits[::2])  # ['apple', 'cherry', 'kiwi']

#10)შეგვიძლია თუ არა რომ for loop - ს გადავცეთ 1 - ზე მეტი არგუმენტი, თუ კი ჩამოთვალეთ ისინი და განიხილეთ თითოეული მათგანი, ასევე თქვენთვის გააკეთეთ 2-2 მაგალითი
names = ["Giorgi", "Nino", "Mari"]

for index, name in enumerate(names):
    print(index, name)



names = ["Giorgi", "Nino", "Mari"]
ages = [16, 12, 17]

for name, age in zip(names, ages):
    print(name, "is", age, "years old")
  
