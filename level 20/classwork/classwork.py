# 1) შექმენით list'ი 5 ელემენტით და slicing'ის მეშვეობით გამოიტანეთ 2 ელემენტიდან ბოლო ელემენტის ჩათვლით

list1 = [2, 51, 11, 13, 51, 100]

print(list1[2:])

animals = ["dog", "cat", "cow", "geraffe"]

print(animals[2:])

food = ["pizza", "fries", "khinkali", "spagetti"]

print(food[2:])

scholl = ["desk", "book", "notebook", "pen"]

print(scholl[2:])

football = ["ball", "boots", "shorts", "T-shirt"]

print(football[2:])

# 2) შექმენით list'ი 5 ელემენტით და slicing'ის მეშვეობით გამოიტანეთ თავიდან ბოლოს წინა ელემენტამდე

football = ["ball", "boots", "shorts", "T-shirt"]

print(football[:2])

scholl = ["desk", "book", "notebook", "pen"]

print(scholl[:2])

food = ["pizza", "fries", "khinkali", "spagetti"]

print(food[:2])

animals = ["dog", "cat", "cow", "geraffe"]

print(animals[:2])

list1 = [2, 51, 11, 13, 51, 100]

print(list1[:2])

# 3) შექმენით string'ი და შემდეგ slicing'ის მეშვეობით შეატრიალეთ უკუღმა

str1 = ["dog", "cat", "cow", "geraffe"]

str1[0] = str1[0][::-1]

print(str1)