# PROBLEM 1 -> Create a Decorator which prints even/odd if a decorated function returns even or odd number.

def return_even_or_odd(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        if results % 2 == 0:
            print(f"The number {results} is even")
        else:
            print(f"The number {results} is odd")
        return results
    return wrapper

@return_even_or_odd
def add(a, b):
    return a+b

@return_even_or_odd
def sub(a, b):
    return a-b

add(2, 4)
sub(4, 3)