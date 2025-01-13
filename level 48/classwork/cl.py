# 1) მიმოიხედეთ ოთახში, აირჩიეთ რაიმე ობიექტი და შექმენით მისი dictionary (მინიმუმ 5 key:value pair უნდა ჰქონდეს)

table = {
    "type": "wooden",  # მაგიდის მასალა
    "color": "brown",  # მაგიდის ფერი
    "size": "120x60 cm",  # მაგიდის ზომა
    "has_drawers": True,  # აქვს თუ არა ალმარი
    "number_of_legs": 4  # მაგიდის ფეხების რაოდენობა
}

# 2) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები

table = {
    "type": "wooden",
    "color": "brown",
    "size": "120x60 cm",
    "has_drawers": True,
    "number_of_legs": 4
}

for key in table:
    print(key)


# 3) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს value'ები

table = {
    "type": "wooden",
    "color": "brown",
    "size": "120x60 cm",
    "has_drawers": True,
    "number_of_legs": 4
}

for value in table.values():
    print(value)


# 4) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები და value'ები ერთად

table = {
    "type": "wooden",
    "color": "brown",
    "size": "120x60 cm",
    "has_drawers": True,
    "number_of_legs": 4
}

for key, value in table.items():
    print(f"{key}: {value}")