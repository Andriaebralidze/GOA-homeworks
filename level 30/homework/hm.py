# 2) გააკეთეთ manual_replace ფუნქცია

def manual_len(s):
    count = 0
    for i in s:
        count += 1
    return count

print(manual_len("1325r1512fasdAsdadadasdadadada"))
print(len("1325r1512fasdAsdadadasdadadada"))


# 3) გააკეთეთ manual_len ფუნქცია

def manual_replace(s1, char, replace_char):
     res = ""

     for i in s1:
         if i == char:
             res += replace_char
         else:
             res += i
     
     return res

print(manual_replace("Hello", "e", "."))
    