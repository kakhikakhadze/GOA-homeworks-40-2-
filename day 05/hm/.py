# a = int(input("შეიყვანე პირველი რიცხვი: "))
# b = int(input("შეიყვანე მეორე რიცხვი: "))

# result_map = {
#     (True, False): "True",
#     (False, True): "False",
#     (False, False): "Other"
# }
# print(result_map[(a > b, a < b)])


# name = input("სახელი: ")
# surname = input("გვარი: ")
# print(["we do not have same names", "we have same name"][name == "გიორგი"])


# name = "გიორგი"
# age = 22

# messages = {
#     (True, True): "we have same names and we are adults",
#     (True, False): "we dont have same names but we are adults",
#     (False, False): "we dont have same names and we are not adults"
# }
# is_adult = age > 18
# name_match = name == "გიორგი"  
# print(messages((is_adult, name_match), ""))


# color = input("საყვარელი ფერი: ")
# color_1 = {
#     "მწვანე": "favorite color is green",
#     "ყვითელი": "favorite color is yellow",
#     "შავი": "favorite color is black"
# }
# print(color_1(color, "other color"))


# num = int(input("შეიყვანე რიცხვი: "))
# print("FOR ციკლით:")
# for i in range(1, num + 1):
#     print(i)
# print("WHILE ციკლით:")
# i = 1
# while i <= num:
#     print(i)
#     i += 1


# num = int(input("შეიყვანე 10-ზე მეტი რიცხვი: "))
# print("ჯამი:", sum(range(5, num + 1)))
# i = 5
# total = 0
# while i <= num:
#     total += i
#     i += 1
# print("ჯამი:", total)


# num = int(input("შეიყვანე 50-ზე მეტი რიცხვი: "))
# print("FOR სტეპით:")
# for i in range(1, num, 5):
#     print(i)
# print("WHILE")
# i = 1
# while i < num:
#     print(i)
#     i += 5