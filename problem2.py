def squares_of_evens(numbers):
    return [x**2 for x in numbers if x % 2 == 0]


numbers = [1, 2, 3, 4, 5]
print(squares_of_evens(numbers))  
