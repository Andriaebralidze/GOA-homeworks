# 2) შექმენით 10 ელემენტიანი list'ი და კომენტარის სახით დანომრეთ (მიუწერეთ ინდექსები). შემდეგ კი უბრალოდ გამოიტანეთ ეკრანზე.

list1 = [2, 51, 11, 13, 51, 100]
#        0  1   2   3   4    5

print(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5])

animals = ["dog", "cat", "cow", "geraffe"]
#            0      1      2        3

print(animals[0], animals[1], animals[2], animals[3])

food = ["pizza", "fries", "khinkali", "spagetti"]
#          0        1         2            3 

print(food[0], food[1], food[2], food[3])

scholl = ["desk", "book", "notebook", "pen"]
#           0       1         2         3

print(scholl[0], scholl[1], scholl[2], scholl[3])

football = ["ball", "boots", "shorts", "T-shirt"]
#             0        1        2          3

print(football[0], football[1], football[2], football[3])

google = ["instagram", "messenger", "facebook", "tiktok"]
#             0             1            2          3

print(google[0], google[1], football[2], google[3])

# 3) პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 დადებითი ინდექსებით. (slicing)

print(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], animals[0], animals[1], animals[2], animals[3])
print(food[0], food[1], food[2], food[3], scholl[0], scholl[1], scholl[2], scholl[3])
print(football[0], football[1], football[2], football[3], google[0], google[1], football[2], google[3])

# 4) პირველ დავალებაში შექმნილი List'იდან გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 უარყოფითი ინდექსებით. (slicing)

print(list1[-6], list1[-5], list1[-4], list1[-3], list1[-2], list1[-1], animals[-4], animals[-3], animals[-2], animals[-1])
print(food[-4], food[-3], food[-2], food[-1], scholl[-4], scholl[-3], scholl[-2], scholl[-1])
print(football[-4], football[-3], football[-2], football[-1], google[-4], google[-3], football[-2], google[-1])

# 5) შექმენით სტრინგი და შეატრიალეთ მისი სიმბოლოები ანუ თუ თავიდან იქნებოდა "Hello" გახდეს "olleH"

str1 = ["Hello"]

str1[0] = str1[0][::-1]

print(str1)