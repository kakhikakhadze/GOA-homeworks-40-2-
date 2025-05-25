def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# ტესტი:
print(factorial(5)) 

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print("------")

# ტესტი:

def hide_string(text):
    return "*" * len(text)

# ტესტი:
print(hide_string("hello"))  

def breakdown_number(n):
    str_num = str(n)
    length = len(str_num)
    parts = []
    for i, digit in enumerate(str_num):
        if digit != "0":
            zeros = length - i - 1
            parts.append(digit + "0" * zeros)
    return " + ".join(parts)

# ტესტი:
print(breakdown_number(1980))  
print(breakdown_number(4025))