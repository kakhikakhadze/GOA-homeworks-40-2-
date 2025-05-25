car = "toyota"
print(car.capitalize())

car2 = "honda"
print(car2.capitalize())

car3 = "mazda"
print(car3.capitalize())


fruit = "banana"
print(fruit.upper())

fruit2 = "apple"
print(fruit2.upper())

fruit3 = "kiwi"
print(fruit3.upper())

country = "FRANCE"
print(country.lower())

city = "tbilisi"
print(city.index("s"))

city2 = "paris"
print(city2.index("s"))

city3 = "brussels"
print(city3.index("s"))

items = ["ირაკლი", "ბექა", 50, "ატამი", 40.50, "თვითმფრინავი"]
print(items.index("ატამი"))
print(items.index(50))

# დამატებითი მაგალითები
items2 = ["გიორგი", 100, "დანა", "წამალი", 3.14]
print(items2.index("დანა"))
print(items2.index(100))

items3 = [200, "კალამი", "სოფო", 99, "ლიმონი"]
print(items3.index("ლიმონი"))
print(items3.index(200))


names = ["dato", "nino", "giorgi"]
new_names = [name.capitalize() for name in names]
print(new_names)

countries = ["georgia", "germany", "spain"]
upper_countries = [country.upper() for country in countries]
print(upper_countries)

countries = ["FRANCE", "USA", "ITALY"]
lower_countries = [country.lower() for country in countries]
print(lower_countries)