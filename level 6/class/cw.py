weather = input("Enter weather: ")

if weather == "sunny":
    print("Wear a Hat")
elif weather == "rainy":
    print("Wear boots")
elif weather == "cloudy":
    print("Wear a jacket")
else:
    print("Wear a T-shirt")


# if და elif

# if – პირველი პირობის შესამოწმებლად
# elif – დამატებითი პირობებისთვის
# ბევრი if-ის გამოყენება ცუდი პრაქტიკაა,
# რადგან ყველა if მოწმდება, ხოლო elif – მხოლოდ საჭირო შემთხვევაში


# მოცემული კოდის ახსნა

name = input('Enter your name: ')  # მომხმარებელი შემოიტანს სახელს
vowels = 'aeiouAEIOU'              # ხმოვნების სია
count = 0                          # მრიცხველი

for i in name:                     # გადავლა სახელის თითოეულ ასოზე
    if i in vowels:                # თუ ასო ხმოვანია
        count = count + 1          # მრიცხველის გაზრდა

print(count)                       # ხმოვნების რაოდენობის დაბეჭდვა


# რატომ არ შეგვიძლია რიცხვზე for loop

# for loop მუშაობს iterable-ებზე (list, string, range)
# რიცხვი iterable არ არის