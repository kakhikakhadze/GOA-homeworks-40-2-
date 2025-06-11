# def გაყოფა_e_ზე(ტექსტი):
#     return ტექსტი.split("ე")

# print(გაყოფა_e_ზე("ალექსანდრე"))

# def ტექსტის_მოჭრა(ტექსტი, რიცხვი):
#     return ტექსტი[:რიცხვი]
# ტექსტის_მოჭრა("ჰიდროელექტროსადგური", 6))  # შედეგი: ჰიდროე

# def სია_სტრინგად(სია):
#     return " ".join(სია)

# print(სია_სტრინგად(["ეს", "არის", "ტექსტი"]))

# def არის_დიდი(სტრინგი):
#     return სტრინგი[0].isupper()

# print(არის_დიდი("Giorgi"))  # True
# print(არის_დიდი("giorgi"))  # False

# def ამოიღე_მცირე(სია):
#     ახალი_სია = [სიტყვა for სიტყვა in სია if len(სიტყვა) >= 5]
#     return ახალი_სია

# print(ამოიღე_მცირე(["ana", "giorgi", "saba", "nika", "alexandre"]))

# def მხოლოდ_Capitalize(სია):
#     ახალი = [სიტყვა for სიტყვა in სია if სიტყვა[0].isupper()]
#     return ახალი

# სია = ["kaxi", "ana", "Aleqsandre", "ia", "Giorgi", "Iamze", "beqa"]
# print(მხოლოდ_Capitalize(სია))