def იპოვე_მინ_მაქს(სია):
    return min(სია), max(სია)
print(იპოვე_მინ_მაქს([10, 22, 5, 67, 89, 1]))

def დაამუშავე_გრძელი_სტრინგები(სია):
    შედეგი = [სიტყვა[::-1].capitalize() for სიტყვა in სია if len(სიტყვა) > 6]
    return შედეგი
print(დაამუშავე_გრძელი_სტრინგები(["hello", "programming", "function", "python"]))

for i in range(1, 101):
    if i % 2 != 0:
        print(i)

i = 1
while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

i = 1
while i <= 50:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1

for i in range(100):
    print("hello")

i = 0
while i < 100:
    print("hello")
    i += 1

