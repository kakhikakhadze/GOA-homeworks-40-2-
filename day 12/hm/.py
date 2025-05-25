# append() - ამატებს ელემენტს ბოლოში
my_list = [1, 2, 3]
my_list.append(4) 

# insert() - ამატებს ელემენტს მითითებულ ინდექსზე
my_list.insert(1, 100)

# extend() - ერთ სიას აერთებს მეორე სიას
a = [1, 2]
b = [3, 4]
a.extend(b)  

# pop() - შლის ელემენტს ინდექსით და აბრუნებს მას
nums = [10, 20, 30]
nums.pop(1)  

# remove() - შლის კონკრეტული მნიშვნელობის ელემენტს
words = ["apple", "banana", "kiwi"]
words.remove("banana") 

# index() - აბრუნებს კონკრეტული ელემენტის ინდექსს
fruits = ["apple", "banana", "kiwi"]
print(fruits.index("kiwi"))

# count() - ითვლის რამდენჯერ გვხვდება ელემენტი
nums = [1, 2, 2, 3]
print(nums.count(2))

# reverse() - აბრუნებს სიის ელემენტებს უკუღმა
a = [1, 2, 3]
a.reverse()  

# sort() - ასორტირებს ზრდადობით (მხოლოდ ერთი ტიპის ელემენტებზე მუშაობს)
nums = [5, 2, 9, 1]
nums.sort()  # [1, 2, 5, 9]

# clear() - ცლის მთელ სიას
items = [1, 2, 3]
items.clear() 

# copy() - ქმნის სიის ასლს
original = [1, 2, 3]
clone = original.copy()

def get_integers(lst):
    result = []
    for item in lst:
        if type(item) == int:
            result.append(item)
    return result

# ტესტი:
print(get_integers(["text", 5, 3.14, True, 10]))  # [5, 10]

def has_square_root(num):
    if num < 0:
        return False  

    root = num ** 0.5
    return root.is_integer()

# ტესტი:
print(has_square_root(16))
print(has_square_root(20))  

def reverse_with_dashes(text):
    reversed_text = ""
    for char in reversed(text):
        reversed_text += char + "-"
    return reversed_text[:-1]  

# ტესტი:
print(reverse_with_dashes("Goa"))  

def collect_words():
    words = []
    while True:
        word = input("შეიტანე სიტყვა: ")
        if word.lower() == "საკმარისია":
            break
        words.append(word)
    return words

def sum_of_divisors(num):
    total = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total += i
    return total

# ტესტი:
print(sum_of_divisors(6))  
print(sum_of_divisors(10))  