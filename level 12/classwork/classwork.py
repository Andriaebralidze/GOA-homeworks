#1) გაიხსენეთ და ახსენით წესები რომლებიც მუშაობს ყველა ლოგიკურ ოპერატორზე რაც დღეს ვისწავლეთ (and, or, not)

#end-ის გამოყენების დროს როდესაც გამოვიყენებთ False არ აქვს არანაირი მნიშვნელობა True-ს დაწერ თუ False-ს მაინც გამოგვიტანს False-ს და ყველა სხვა კომბინაცია გამოგვიტანს true-ს
#or-ის გამოყენების დროს თუ რომელიმე ადგილას გამოვიყენებთ true-ს ყოველთვის გამოიტანს True-ს ხოლო ყველა სხვა კომბინაცია ნიშნავს False-ს
#not-ის გამოყენებისას (not True)-ნისნავს False-ს ხოლო (not False)ნიშნავს True-ს


#2) შექმენით and ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი

print(False and True)
print(True and False)
print(True and True)
print(False and False)
print(True and True and False and True)

#3) შექმენით or ოპერატორის მეშვეობით 5 სხვადასხვა მაგალითი


print(True or True)
print(False or False)
print(False or True)
print(True or False)
print(False or False or True or False)

#4) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ 5 მაგალითი

print(5 > 4 and True)  #True
print(8 > 10 and True)  #False
print(14 < 21 and False)  #False
print(21 > 20 and 80 < 30 and True) #False
print(81 > 369 and 69 < 169)  #False