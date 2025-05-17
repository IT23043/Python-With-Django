#https://github.com/IT23043/Python-With-Django/blob/main/Assignment-1/IMG_20250517_103142.jpg
n = int(input("Enter an odd number (n): "))
sum = 0
for i in range(1, n + 1, 2):
    sum = sum + (i ** 2)
print("Sum of series: ", sum)
