# 1) დღეს რომელი ფუნქციები და მეთოდები ვისწავლეთ, გატესტეთ ყველა: len(), .append(), .insert(), .pop(), .remove()

print(len("andria ebralidze"))


sports = ["football", "basketball", "rugby"]
sports.append("tennis")
print(sports)


sports = ["football", "basketball", "rugby"]
sports.insert(2, "tennis")
print(sports)


sports = ["football", "basketball", "rugby"]
sports.pop(2)
print(sports)


sports = ["football", "basketball", "rugby"]
sports.remove("rugby")
print(sports)

# 2) .pop() მეთოდის გამოყენებით გამოაცალკევეთ კონკრეტული ელემენტი list'ისგან და ჩასვით ცალკე ცვლადში ზუსტად ისე როგორც მე გავაკეთე

sports = ["football", "basketball", "rugby"]

x = sports.pop(2)
print(x)

# 3) ახსენით განხსვავება pop'სა და remove'ს შორის

# remove - მოითხოვს ფრჩიხელბში მინიმუმ ერთი არგუმენტის ჩაწერას ხოლო პოპი არა

# 4) შექმენით 4 ელემენტიანი list'ი და შუაში ჩაამატეთ 1 ელემენტი

sports = ["football", "basketball", "rugby" , "swimming"]
sports.insert(2, "tennis")
print(sports)