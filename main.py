numbers = list(range(1, 21))
squares = [number ** 2 for number in numbers]
evens = [number for number in numbers if number % 2 == 0]
even_squares = [number ** 2 for number in numbers if number % 2 == 0]
labels = ["even" if number % 2 == 0 else "odd" for number in numbers]
grid = [[row * column for column in range(1, 4)] for row in range(1, 4)]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", evens)
print("Squares of even numbers:", even_squares)
print("Parity labels:", labels)
print("3 x 3 multiplication grid:", grid)
