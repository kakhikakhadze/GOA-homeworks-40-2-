def replace_letters(word):
    vowels = "aeiouAEIOUაეიოუAEIOU" 
    result = ""
    for char in word:
        if char.isalpha():
            if char in vowels:
                result += "!"
            else:
                result += "*"
        else:
            result += char
    return result

# ტესტი:
print(replace_letters("Goa123!"))

def check_license(name, age):
    my_name = "giorgi"  
    if age > 18 and name.lower() == my_name:
        return "თქვენ წარმატებით აიღეთ მართვის მოწმობა"
    else:
        return "თქვენ ჩაიჭერით"

# ტესტი:
print(check_license("Giorgi", 20))
print(check_license("Nino", 17))

def split_float(num):
    integer_part = int(num)
    decimal_part = round(num - integer_part, 2)
    return f"{integer_part} + {decimal_part}"

# ტესტი:
print(split_float(19.27))  

def collect_and_filter():
    result = []
    while True:
        word = input("შეიყვანე სიტყვა: ")
        if word.lower() == "საკმარისია":
            break
        if len(word) <= 5 and any(char.isdigit() for char in word):
            result.append(word)
    return result
