#2) კომენტარების სახით ახსენით თუ რა არის default parameters - რაში გამოვიყენებთ ჩვენ მას, რას აკეთებს return
# Default parameter — ეს არის არგუმენტი, რომელსაც აქვს თავისი ნაგულისხმევი (default) მნიშვნელობა.
# თუ ფუნქციას ეს არგუმენტი არ გადავეცით, მაშინ ავტომატურად გამოიყენება default value.
# Default parameters ვიყენებთ მაშინ, როცა გვინდა ფუნქციას ჰქონდეს "სარეზერვო" მნიშვნელობა.

def greet(name="User"):  
    return "Hello " + name

# return — აბრუნებს მნიშვნელობას ფუნქციიდან.
# ის წყვეტს ფუნქციის მუშაობას და აბრუნებს შედეგს, რომ შემდგომ გამოიყენოთ.




#3) შექმენით ფუნქცია სახელად which_is_greater რომელიც იღებს ორ არგუმენტს, თქვენი დავალებაა, რომ შეამოწმოთ თუ რომელია ამ ორი რიცხვიდან დიდი, თუ პირველი რიცხვი მეორეზე მეტია გამოიტანეთ message - The first number is greater than the second number, თუ მეორე მეტია პირველზე გამოიტანეთ The second number is greater than the first number სხვა შემთხვევაში კი they are equal to each other
def which_is_greater(a, b):
    if a > b:
        print("The first number is greater than the second number")
    elif b > a:
        print("The second number is greater than the first number")
    else:
        print("They are equal to each other")

#4) შექმენით ფუნქცია სახელად sum რომელიც არგუმენტად იღებს მასივს, თქვენი დავალებაა, რომ გამოიტანოთ ამ მასივში არსებული რიცხვების ჯამი
def sum(numbers):
    total = 0  # აქ ინახება ჯამი
    for num in numbers:
        total += num
    print(total)

#5) შექმენით ფუნქცია სახელად count_vowels რომელიც იღებს ერთ არგუმენტს, თქვენი დავალებაა, რომ დაითვალოთ გადმოცემული ტექსტის ხმოვნების რაოდენობა
def count_vowels(text):
    vowels = "aeiouAEIOU"  # ხმოვნები (დიდი და პატარა)
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    print(count)

#6) შექმენით ფუნქცია სახელად is_palindrome რომელიც იღებს string - ს, თქვენი დავალებაა, რომ შეამოწმოთ არის თუ არა გადმოცემული string - ი palindrome, თუ არის მაშინ გამოიტანეთ მნიშვნელობა 'This text is palindrome' სხვა შემთხვევაში კი 'This text is not a palindrome'
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()  
    if cleaned == cleaned[::-1]:  # 
        print("This text is palindrome")
    else:
        print("This text is not a palindrome")

#palindrome meaning ---> a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.
def is_uppercase(text):
    return text.isupper()  # აბრუნებს True ან False

#7) შექმენით ფუნქცია სახელად is_uppercase რომელიც იღებს string - ს, თქვენი დავალებაა, რომ შეამოწმოთ არის თუ არა მოცემული ტექსტი მაღალ რეგისტრში თუ არის დააბრუნეთ True სხვა შემთხვევაში False
def is_uppercase(text):
    return text.isupper()  # აბრუნებს True ან False

#8) გააკეთეთ list, string methods - ებზე რამოდენიმე მაგალითი
numbers = [1, 2, 3, 4]

numbers.append(5)      
numbers.remove(2)      
numbers.reverse()     

print(numbers)


#9) შექმენით ფუნქცია სახელად remove_duplicates რომელიც არგუმენტად იღებს მასივს, თქვენი დავალებაა, რომ მოცემული მასივიდან ამოიღოთ ყველა ისეთი ელემენტი რომელიც მეორდება ერთზე მეტჯერ
def remove_duplicates(arr):
    result = []  
    for item in arr:
        if item not in result: 
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))
