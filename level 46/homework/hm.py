# შექმენით ფუნქცია რომელიც გააქრობს დუპლიკატებს string'იდან (გამოიყენეთ set()) 


def remove_duplicates_with_set(str1):
    return "".join(sorted(set(str1)))

print(remove_duplicates_with_set("abcdefgabcdefg"))