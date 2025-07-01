from math import factorial, e

def e_x(x, terms=10):
    total = 0
    for i in range(terms):
        total += (x ** i) / factorial(i)
    return total

x = int(input("Enter x: "))
for n in range(1, 100):
    approx = e_x(x, n)
    true_val = e ** x
    print(f"e^{x} (for {n} terms) = {approx}")
    print(f"Truncation Error = {true_val - approx} for {n} terms")
