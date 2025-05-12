names = ["ნინო", "ლევანი", "ანა", "მარიამი", "გიორგი"]
print(names[0])  
print(names[-1])  


names = ["ლაშა", "გიორგი", "თამარი", "ნინო"]
# -4 -> ლაშა
# -3 -> გიორგი
# -2 -> თამარი
# -1 -> ნინო


names = ["სოფო", "ბექა", "თათია"]
for name in names:
    print(name)


text = "Akaki"
for letter in text:
    print(letter)


list= ["ლუკა", "ანა", "ნიკა", "ელენე", "გიგა", "მარი", "გიო", "დათო", "ნანა", "კეკე"]
print(names[2:8])


city = "konstantinopoli"
print(city[-8:])  


fruits = ["ვაშლი", "მსხალი", "ბანანი"]
fruits[0] = "საქართველო"
fruits[1] = "იტალია"
fruits[2] = "საფრანგეთი"
print(fruits)


word = "banana"
new_word = word[:-1] + "k"
print(new_word)


numbers = [10, 5, 20, 40]
print(sum(numbers))