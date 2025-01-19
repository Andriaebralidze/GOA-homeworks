# 1) რომლებია mutable მონაცემთა ტიპები?
# mutable ტიპი არის მაგალითდ list'ი და set'ი

# 2) რომლებია immutable მონაცემთა ტიპები?
# immutable ტიპი არის მაგალითად string'ი და tuple'ი

# 3) რა ეწოდება lambda ფუნქციას მეორენაირად?
# ლამბადა ფუნქციას მეორენაირად ეწოდება ანონიმური ფუნქცია

# 4) რა განსხვავებაა map'სა და filter'ს შორის?
# map'ი ყველა ელემენტს ცვლის ფუნქციის მიხედვით და filter'ი false'ებს აშორებს და მარტო true'ებს ტოვებს

# 5) რა ჰქვია ორი სტრინგის შეერთებას?
# ორი სტრინგის შეერთებას ეწოდება კონკატენაცია

# MAPS

# 1) გამოიყენეთ map ფუნქცია რომ შექმნათ list'ი სადაც იქნება ამ რიცხვების კვადრატები: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
num1 = list(map(lambda x: x ** 2, numbers))
print(num1)

# 2) დაწერეთ პროგრამა mapის გამოყენებით რომ გადაიყვანოთ ამ list'ში მოცემული celsius'ები fahrenheit'ში: [0, 20, 30, 40] (1 celsius == 33.8 fahrenheit)

celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda x: x * 1.8 + 32, celsius))
print(fahrenheit)

# 3) გამოიყენეთ map ფუნქცია რომ გაადიდოთ ყველა სიტყვის პირველი ასო ამ list'ში: ["hello", "world", "python"]

words = ["hello", "world", "python"]
capitalized_words = list(map(lambda x: x[0].upper() + x[1:], words))
print(capitalized_words)

# FILTERS

# 1) გამოიყენეთ filter ფუნქცია რომ ამოწეროთ მხოლოდ ლუწი რიცხვები list'იდან: [1, 2, 3, 4, 5, 6, 7, 8].

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 2) დაწერეთ პროგრამა filterის გამოყენებით რომ ამოწეროთ ისეთი string'ები რომლებიც შეიცავენ 4 სიმბოლოს ან მასზე მეტს: ["cat", "house", "tree", "car"].

words = ["cat", "house", "tree", "car"]
long_words = list(filter(lambda x: len(x) >= 4, words))
print(long_words)

# 3) გამოიყენეთ filter ფუნქცია რომ ამოწეროთ სამის ჯერადი რიცხვები: [3, 9, 15, 22, 27, 30]. 

numbers = [3, 9, 15, 22, 27, 30]
multiples_of_three = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_three)