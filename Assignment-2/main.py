# https://github.com/IT23043/Python-With-Django/blob/main/Assignment-2/IMG_20250517_105431.jpg
import Calc as c

a = int(input("Enter a: "))
b = int(input("Enter b: "))

while True:
    choice = int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or -1 to exit: "))

    if choice == -1:
        print("Exiting program.")
        break
    elif choice == 1:
        print(a, "+", b, "=", c.add(a, b))
    elif choice == 2:
        print(a, "-", b, "=", c.sub(a, b))
    elif choice == 3:
        print(a, "*", b, "=", c.multiply(a, b))
    elif choice == 4:
        print(a, "/", b, "=", c.divide(a, b))
    else:
        print("Invalid choice. Please try again.")
