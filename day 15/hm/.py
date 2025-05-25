def odd_index_chars(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 1:
            result += text[i]
    return result

# ტესტი:
print(odd_index_chars("aleqsandre"))

def even_numbers_only(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# ტესტი:
print(even_numbers_only([1, 2, 3, 4, 5, 6]))  

def char_indexes(text):
    indexes = []
    count = 0
    for _ in text:
        indexes.append(count)
        count += 1
    return indexes

# ტესტი:
print(char_indexes("fortoxali")) 

def name_indexes(names):
    result = []
    count = 0
    for _ in names:
        result.append(count)
        count += 1
    return result

# ტესტი:
print(name_indexes(["nino", "luka", "saba"]))  

def remove_odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# ტესტი:
print(remove_odd_numbers([1, 2, 3, 4, 5, 6, 7])) 