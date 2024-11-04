# 2) შექმენით ფუნქცია რომელიც დააბრუნებს "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount"

def adult_check(age):
     if age >=18:
         return "You got discount"
     else:
         return "You didn't get discount"
    

# 3) შექმენით ფუნქცია manual_reverse, რომელიც არგუმენტად მიიღებს string'ს და დააბრუნებს ამ string'ს ოღონდ შეტრიალებულად

s = "ANDRIA"
s = s[::-1]

# 4) გატესტეთ .upper(), .lower(), .capitalize(), .swapcase() და .find() მეთოდები

s = "andria"
s = s.upper()

print(s)


s = "andria"
s = s.find("a")

print(s)

s = "aNdRiA"
s = s.swapcase()

print(s)

s = "andria"
s = s.capitalize()

print(s)

s = "ANDRIA"
s = s.lower()

print(s)

# 5) ახსენით რატომ ჰქვიათ ამ ფუნქციებს მეთოდები

# .upper() - გამოაქვს წინადადება დიდი ასოებით
#.lower() - გამოაქვს წინადადება პატარა ასოებით
#.capitalize() - იწყებს წინადადებას დიდი ასოთი, სხვა დანარჩენს კი აპატარავებს
#.swapcase() - დიდი ასო გამოაქვს პატარად და პატარა დიდად

# 6) ახსენით რა არის dot notation და რა შემთხვევაში გამოიყენება

# ზოგიერთი ფუქნცია იწერება დოტ ნოტაციით, რაც იმას ნიშნავს, რომ ჯერ ხდება ცვლადის სახელის დაწერა შემდეგ, წერტილი და ფუნქციის სახელი