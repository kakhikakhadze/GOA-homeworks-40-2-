# ქეის სენსიტიური - ნიშნავს რომ სიმბოლოების მცირე და დიდი ასოები განსხვავებულია. მაგ: "Name" და "name" განსხვავდება.
# string - ტექსტური ტიპის მონაცემია, მაგ: "სალამი"
# float - ათწილადი რიცხვია, მაგ: 3.14
# boolean - True ან False ტიპის მნიშვნელობა
# integer - მთელი რიცხვი, მაგ: 10
# list - სია, სადაც შეგვიძლია შევინახოთ მრავალი მონაცემი ერთდროულად, მაგ: [1, 2, 3] ან ["ა", "ბ", "გ"]

# def მიბრძანდი_სახელი(სახელი):
#     ჩემი_სახელი = "გიორგი"
#     if სახელი.lower() == ჩემი_სახელი.lower():
#         return f"გამარჯობა {სახელი}!, სასიამოვნოა თქვენი გაცნობა."
#     else:
#         return f"გამარჯობა {სახელი}!"

# def დაახლიჩე_a_ზე(სიტყვა):
#     ნაწილები = სიტყვა.split("a")
#     return ნაწილები

# def სახელების_შემოტანა():
#     ჩემი_სახელი = "გიორგი"
#     სია = []
#     while True:
#         სახელი = input("შეიყვანე სახელი: ")
#         სია.append(სახელი)
#         if სახელი.lower() == ჩემი_სახელი.lower():
#             break
#     return სია, len(სია)

# def სიტყვების_შემოტანა():
#     სია = []
#     რიცხვი = int(input("შეიყვანე რიცხვი: "))
#     while True:
#         სიტყვა = input("შეიყვანე სიტყვა (ან დაწერე 'გაჩერდი!'): ")
#         სია.append(სიტყვა)
#         if სიტყვა == "გაჩერდი!":
#             break
#     შედეგი = სია[:რიცხვი+1]  # "+1", რომ ჩათვალოს ის პოზიციაც
#     return შედეგი