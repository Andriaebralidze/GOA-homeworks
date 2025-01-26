# 1) შექმენით რაიმე list'ი რომელშიც იქნება integer'ები და შემდეგ ამოწერეთ მხოლოდ ისეთი რიცხვები რომლებიც მეტია ან ტოლია 40'ის.

numbers = [12, 45, 30, 67, 22, 55, 40, 89, 33, 41]
filtered_numbers = list(filter(lambda num: num >= 40, numbers))
print(filtered_numbers)

# 2) შექმენით რაიმე list'ი რომელშიც იქნება integer'ები და შემდეგ გამოიტანეთ list'ი სადაც იქნება ყველა რიცხვის კვადრატი

numbers = [2, 4, 6, 8, 10]
squared_numbers = list(map(lambda num: num ** 2, numbers))
print(squared_numbers)

# 3) შექმენით რაიმე list'ი რომელშიც იქნება string'ები და შემდეგ ამოწერეთ მხოლოდ ისეთები რომლებიც მთავრდება "a" სიმბოლოთი.

food = ["apple", "banana", "kiwi", "strawberry"]
words_ending_with_a = list(filter(lambda word: word.endswith("a"), food))
print(words_ending_with_a)