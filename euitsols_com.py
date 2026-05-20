a = 10
b = 20

print("Before swap:")
print("a =", a)
print("b =", b)

a, b = b, a   # swapping

print("After swap:")
print("a =", a)
print("b =", b)

#2. FizzBuzz (1 to 30)
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#3. Grade Calculator

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(get_grade(90))
print(get_grade(70))
print(get_grade(45))

#4. Even Numbers Sum (1 to 100)
def factorial(n):
    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1

    return result

print(factorial(5))
print(factorial(0))

#5. Factorial Function (while loop)
def factorial(n):
    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1

    return result

print(factorial(5))
print(factorial(0))