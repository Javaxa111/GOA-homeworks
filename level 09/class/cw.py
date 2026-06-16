# პარამეტრი – ფუნქციის აღწერისას
# არგუმენტი – ფუნქციის გამოძახებისას


def greet(name):
    print("Hello", name)

greet("Gio")


def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(7)


def count_number(arr, num):
    count = 0
    for i in arr:
        if i == num:
            count += 1
    return count

numbers = [1, 2, 3, 2, 4, 2]
print(count_number(numbers, 2))