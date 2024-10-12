#2) გააკეთეთ and ოპერატორის 10 მაგალითი და სანამ გაუშვებთ კომენტარად მიაწერეთ თქვენი აზრით რა იქნება შედეგი (არ არის აუცილებელი მხოლოდ 2 Input'ი იყოს, შეიძლება იყოს 10'იც, ანუ მაგალითად: True and True and False and False and True (5 input))

print(False and True)  #False
print(True and False)  #False
print(True and True)   #True
print(False and False)   #False
print(True and True and False and True)   #False
print(False and True and False and True)   #False
print(True and True and True and True  and True)  #True
print(True and True and True and False)  #False
print(False and False and True and True)  #False 
print(True and True and True and True and True and False and True and True)  #False


#3) გააკეთეთ or ოპერატორის 10 მაგალითი და სანამ გაუშვებთ კომენტარად მიაწერეთ თქვენი აზრით რა იქნება შედეგი


print(True or True)  #True
print(False or False)  #False
print(False or True)  #True
print(True or False)  #True
print(False or False or True or False)  #True
print(False or False or False or False or False or False or False)  #False
print(True or True or True or True or True or True or True)  #True
print(False or False or False or True or False or False)  # True
print(True or False or True or False or True or False or True or False)  #True
print(False or False or False or False or False)  #False

#4) შეურიეთ or და and ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად

print(True and False or True and False)  #False
print(True or False or True or False or True and False )  #True
print(False and True or False)  #False
print(True and False or True and True)  #True
print(False or False or False or True and False)  #Fasle
print(True or False and True and True and False or True)  #True 
print(True or False or False and True and False and True or True)  #True
print(False or False or False and True and False and True )  #False
print(True and False or False )  #False
print(False or True or False or True and False)  #True



#5) შეურიეთ შედარების და ლოგიკური ოპერატორები და გააკეთეთ ისევ 10 მაგალითი წინა დავალებების მსგავსად

print(5 > 4 and True)  #True
print(8 > 10 and True)  #False
print(14 < 21 and False)  #False
print(21 > 20 and 80 < 30 and True) #False
print(81 > 369 and 69 < 169)  #False
print(15 < 25 and 33 < 48 and 55 < 70 and 86 < 105)  #True
print(150 < 222 and 280 > 315 and 180 < 7)  #False
print(6754 < 723 and 873 > 7281 and 82356 > 91367)  #False
print(9164371362 > 92637312 and 29 > 24 and 2963 > 243) #True
print(2845386 >263 and 9263 <12873 and 2853>27368)  #False