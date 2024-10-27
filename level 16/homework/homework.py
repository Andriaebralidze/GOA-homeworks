# 2) გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

result = 1

for i in range(1, 10 + 1):
    result = result * i
print(result)

# 3) გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

result = 1
num = 1

while num < 20 + 1:
    result = result * num
    num = num + 1

print(result)

 # 4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:       10 % 2 = 0;        5 % 2 = 1)

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Your number is Even")
else:
    print("Your number is Odd")

# 5) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ ფოტოს მიხედვით: (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)

student_score = int(input("Please enter your score: "))

if student_score >= 90 and student_score <= 100:
    print("Your grade is A")
elif student_score >= 80 and student_score <= 90:
    print("Your grade is B")
elif student_score >= 70 and student_score <= 80:
    print("Your grade is C")
else:
    print("Your grade is D")