n = int(input("Enter an odd number (n): "))
sum = 0
for i in range(1, n + 1, 2):
    sum = sum + (i ** 2)
print("Sum of series: ", sum)
