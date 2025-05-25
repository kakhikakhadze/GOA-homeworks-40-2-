
# data = ["text", 42, 3.14, True, None, [1, 2], {"a": 1}]
# data.append("ახალი ელემენტი")
# print(data)

# # დამატებითი მაგალითები
# example1 = [10, "hello", False]
# example1.append(99.99)
# print(example1)

# example2 = ["start", 123, None]
# example2.append(["another", "list"])
# print(example2)

# info = ["apple", 23, True, 5.6, None, {"x": 1}, [4, 5]]
# info.insert(3, "inserted1")
# info.insert(5, 77)
# info.insert(7, False)
# print(info)

# # დამატებითი მაგალითები
# ex1 = [1, 2, 3, 4]
# ex1.insert(1, "hello")
# ex1.insert(3, 8.8)
# print(ex1)

# ex2 = ["a", "b", "c"]
# ex2.insert(0, "start")
# ex2.insert(2, 100)
# print(ex2)



# # ორივე ფუნქცია გამოიყენება სიაში ახალი ელემენტის დამატებისთვის.

# # append() – ყოველთვის ამატებს ელემენტს სიის ბოლოში.
# # insert() – ამატებს ელემენტს კონკრეტულ ინდექსზე, რომელიც თავად უნდა მიუთითოთ.

# items = [10, "hello", 3.14, True, None, [1, 2], "end"]
# items.pop(3)
# items.pop(2)
# items.pop(5)  # ამ შემთხვევაში ბოლო ინდექსია
# print(items)

# # დამატებითი მაგალითები
# a = ["x", "y", "z", 100, 200]
# a.pop(1)
# print(a)

# b = [5, 10, 15, 20]
# b.pop(0)
# print(b)

# mixed = ["data", 42, 3.14, True, None, "remove me", 99]
# mixed.remove("data")
# mixed.remove(3.14)
# mixed.remove(99)
# print(mixed)


# lst1 = [1, 2, 3, 2, 4]
# lst1.remove(2)
# print(lst1)

# lst2 = ["apple", "banana", "cherry"]
# lst2.remove("banana")
# print(lst2)


# # ორივე ფუნქცია გამოიყენება სიიდან ელემენტების წასაშლელად.

# # განსხვავება:
# # pop() – შლის ელემენტს ინდექსის მიხედვით და აბრუნებს ამოშლილ მნიშვნელობას.
# # remove() – შლის კონკრეტულ მნიშვნელობას სიიდან, მაგრამ არ აბრუნებს.

# strings = ["apple", "banana", "kiwi"]
# integers = [1, 2, 3]

# strings.extend(integers)
# print(strings)

# floats = [1.1, 2.2, 3.3]


# strings.extend(floats)
# print(strings)


# # გაიარე სოლოლერნზე (SoloLearn) Python-ის კურსი – განსაკუთრებით სექცია სიებზე (list),
# # და მათი ფუნქციები: append, insert, pop, remove, extend, და სხვ. დაგეხმარება პრაქტიკაში.
