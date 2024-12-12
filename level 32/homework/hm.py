# 2) გააკეთეთ manual_find ფუნქცია

def manual_find(s, i):
    y = 0
    for x in s:
        if i == x:
            return y
        else:
            y = y + 1
    return -1

print(manual_find("hello world", "o"))

# 3) გააკეთეთ manual_swapcase ფუნქცია

def manual_swapcase(s):
    res = ""

    for i in s:
        if i == i.lower():
            res = res + i.upper()
        else:
            res = res + i.lower()

    return res

print(manual_swapcase("HeLlo wOrLd"))
