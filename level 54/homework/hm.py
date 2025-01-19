# 2) Use the map function to double the numbers in a list: [2, 4, 6, 8, 10].

numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# 3) Write a program using map to concatenate "Hello, " to each name in a list: ["Alice", "Bob", "Charlie"].

names = ["Alice", "Bob", "Charlie"]
greeted_names = list(map(lambda name: "Hello, " + name, names))
print(greeted_names)

# 4) Use map to calculate the lengths of strings in a list: ["apple", "banana", "kiwi"].

fruits = ["apple", "banana", "kiwi"]
lengths = list(map(len, fruits))
print(lengths)

# 5) Use the filter function to keep only positive numbers from a list: [-5, 3, -2, 7, 0, 10].

numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

# 6) Write a program using filter to extract words starting with the letter "p" from a list: ["pear", "apple", "peach", "grape"].

words = ["pear", "apple", "peach", "grape"]
words_starting_with_p = list(filter(lambda word: word.startswith('p'), words))
print(words_starting_with_p)

# 7) Use filter to find numbers greater than 50 in a list: [10, 55, 42, 78, 65, 20].

numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)