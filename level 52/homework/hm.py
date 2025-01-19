# 2) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც აბრუნებს 2 სტრინგის ჯამს

concat_strings = lambda str1, str2: str1 + str2

print(concat_strings("hello", " world"))

# 3) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც აბრუნებს 3 რიცხვის ჯამს

sum_of_three = lambda x, y, z: x + y + z

print(sum_of_three("hello", " world", " worlds"))

# 4) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც არგუმენტად იღებს list'ს და აბრუნებს მასში მყოფი რიცხვების ჯამს

sum_of_list = lambda list1: sum(list1)

print(sum_of_list([1, 2, 3, 4, 5]))

# 5) შექმენით ცვლადი რომელსაც მნიშვნელობად მისცემთ lambda ფუნქციას რომელიც არგუმენტად იღებს string'ს და რაიმე სიმბოლოს და აბრუნებს რამდენჯერ მეორდება სიმბოლო string'ში

count_char = lambda s, char: s.count(char)

print(count_char("hellllloooooo", "o"))