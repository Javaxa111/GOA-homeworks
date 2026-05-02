# Task 12: Sum of Even Numbers from 1 to 10
# Instructions:
#  Use a for loop with range() to calculate the sum of all even numbers from 1 to 10 and store it in result.
# Test Cases:
# assert result == 30

total=0
for i in range(0, 12, 2):
    total+=i
print(total)        