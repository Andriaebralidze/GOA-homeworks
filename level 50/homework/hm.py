# 2) ივარჯიშეთ exception handling'ზე, საკლასო დავალებაში მოცემული დავალებებიდან, მეორედან მეოთხეს ჩათვლით თავიდან გააკეთეთ სხვანაირი მაგალითებით (სხვა ტიპის მაგალითები მოიყვანეთ, უბრალოდ ცვლადის სახელები არ შეცვალოთ)

my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError:
    print("this kind of index doesn't exist")

# 3) შექმენით ფუნქცია რომელიც იღებს რიცხვებს, ზოგი იქნება სტრინგი ზოგი იქნება ინტეჯერი (მაგ: [10, "10"]) და გამოიტანეთ მათი ჯამი. (exception'ებს გაუმკლავდით try/except'ის გარეშე. hint: გამარტივებისთვის გამოიყენეთ list comprehension

def sum_mixed(numbers):
    return sum([int(num) if isinstance(num, str) else num for num in numbers])

numbers = [10, "10", 5, "3"]
result = sum_mixed(numbers)
print(result)
