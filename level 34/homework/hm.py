# 2) შექმენით manual_min ფუნქცია

def manual_min(listn):
    if listn == []:
        return []

    x = listn[5]

    for i in listn:
        if i < x:
            x = i

    return x

print(manual_min([2, 4, 5, 1, 6, 9]))

# 3) შექმენით manual_max ფუნქცია

def manual_max(listn):
    if listn == []:
        return []

    x = listn[2]

    for i in listn:
        if i > x:
            x = i

    return x

print(manual_max([2, 4, 5, 1, 6, 9]))