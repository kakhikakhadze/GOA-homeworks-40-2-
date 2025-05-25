
def odd_index_letters(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 1:
            result += text[i]
    return result
# ტესტი:
print(odd_index_letters("aleqsandre")) 


# ტესტი:
print(get_even_numbers([1, 2, 3, 4, 5, 6])) 

def get_indexes_from_string(text):
    indexes = []
    index = 0
    for _ in text:
        indexes.append(index)
        index += 1
    return indexes

# ტესტი:
print(get_indexes_from_string("fortoxali"))

def get_name_indexes(names):
    indexes = []
    i = 0
    for _ in names:
        indexes.append(i)
        i += 1
    return indexes

# ტესტი:
print(get_name_indexes(["nino", "dato", "luka"]))  

def remove_odd_numbers(numbers):
    filtered = []
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
    return filtered

# ტესტი:
print(remove_odd_numbers([10, 7, 5, 8, 2, 3])) 