# 2) შექმენით ფუნქცია რომელიც დააბრუნებს "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount"

def adult_check(age):
     if age < 18:
         return "You got discount"
     else:
         return "You didn't get discount"
     
print(adult_check(16))
    

# 3) შექმენით ფუნქცია manual_reverse, რომელიც არგუმენტად მიიღებს string'ს და დააბრუნებს ამ string'ს ოღონდ შეტრიალებულად

def Manual_Reverse(string1):
    return string1[::-1]

print(Manual_Reverse("andria"))

# 4) გატესტეთ .upper(), .lower(), .capitalize(), .swapcase() და .find() მეთოდები

print("andria".upper())

print("ANDRIA".lower())

print("andria".capitalize())

print("andria".swapcase())

print("andria".find("a"))

# 5) ახსენით რატომ ჰქვიათ ამ ფუნქციებს მეთოდები

# .upper() - გამოაქვს წინადადება დიდი ასოებით
#.lower() - გამოაქვს წინადადება პატარა ასოებით
#.capitalize() - იწყებს წინადადებას დიდი ასოთი, სხვა დანარჩენს კი აპატარავებს
#.swapcase() - დიდი ასო გამოაქვს პატარად და პატარა დიდად

# 6) ახსენით რა არის dot notation და რა შემთხვევაში გამოიყენება

# ზოგიერთი ფუქნცია იწერება დოტ ნოტაციით, რაც იმას ნიშნავს, რომ ჯერ ხდება ცვლადის სახელის დაწერა შემდეგ, წერტილი და ფუნქციის სახელი