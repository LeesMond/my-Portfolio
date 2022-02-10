from tkinter import*


print("성적을 입력해 주세요")

question1 = int(input("파이썬 중간.기말 성적을 입력하세요"))
if question1 > 60:
    int(input("\n60점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question11 = int(input("파이썬 과제 성적을 입력해주세요"))
if question11 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question12 = int(input("파이썬 출석 성적을 입력해수세요"))
if question12 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question2 = int(input("전장기초의 중간.기말성적을 입력해주세요"))
if question2 > 60:
    int(input("\n60점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question21 = int(input("전장기초의 과제 성적을 입력해주세요"))
if question21 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question22 = int(input("전장기초의 출석 성적을 입력해주세요"))
if question22 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question3 = int(input("HTML5의 중간.기말성적을 입력해주세요"))
if question3 > 60:
    int(input("\n60점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")
    
question31 = int(input("HTML5의 과제 성적을 입력해주세요"))
if question31 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question32 = int(input("HTML5의 출석 성적을 입력해주세요"))
if question32 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question4 = int(input("디자인과 인간생활의 중간.기말성적을 입력해주세요"))
if question4 > 60:
    int(input("\n60점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question41 = int(input("디자인과 인간생활의 과제 성적을 입력해주세요"))
if question41 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n다음으로")

question42 = int(input("디자인과 인간생활의 출석 성적을 입력해주세요"))
if question42 > 20:
    int(input("\n20점이하로 다시 입력해주세요"))
else:
    print("\n\n\n\n 계산완료")

total1= question1 + question11 + question12;

total2= question2 + question21 + question22;

total3= question3 + question31 + question32;

total4= question4 + question41 + question42;

total= total1 + total2 + total3 + total4;

total5= (total1 + total2 + total3 + total4)/4;

print("\n\n\n")

if total1 >= 90:
    print("파이썬 성적은 'A'",total1)

elif total1 >= 80:
    print("파이썬 성적은 'B'",total1)
elif total1 >= 70:
    print("파이썬 성적은 'C' ",total1)
elif total1 >= 60:
     print("파이썬 성적은 'D' ",total1)
else:
    print("파이썬 성적은 'F'",total1)

print("\n")

if total2 >= 90:
    print("전장기초의 성적은 'A'",total2)

elif total2 >= 80:
    print("전장기초의 성적은 'B'",total2)
elif total2 >= 70:
    print("전장기초의 성적은 'C' ",total2)
elif total2 >= 60:
     print("전장기초의 성적은 'D' ",total2)
else:
    print("전장기초의 성적은 'F'",total2)


print("\n")

if total3 >= 90:
    print("HTML5의 성적은 'A'",total3)

elif total3 >= 80:
    print("HTML5의 성적은 'B'",total3)
elif total3 >= 70:
    print("HTML5의 성적은 'C' ",total3)
elif total3 >= 60:
     print("HTML5의 성적은 'D' ",total3)
else:
    print("HTML5의 성적은 'F'",total3)

print("\n")

if total4 >= 90:
    print("디자인과 인간생활의 성적은 'A'",total4)
    
elif total4 >= 80:
    print("디자인과 인간생활의 성적은 'B'",total4)
elif total4 >= 70:
    print("디자인과 인간생활의 성적은 'C' ",total4)
elif total4 >= 60:
     print("디자인과 인간생활의 성적은 'D' ",total4)
else:
    print("디자인과 인간생활의 성적은 'F'",total4)

print("\n\n\n")

if total >= 360:
    print("\n전체 성적은 'A'","\n전체성적합:",total,"\n전체 성적합의 평균:",total5)
elif total >= 320:
    print("전체 성적은 'B'","\n전체성적합:",total,"\n전체 성적합의 평균:",total5)
elif total >= 280:
    print("전체 성적은 'C'","\n전체성적합:",total,"\n전체 성적합의 평균:",total5)
elif total >= 240:
    print("전체성적은 'D'","\n전체성적합:",total,"\n전체 성적합의 평균:",total5)
else:
    print("전체 성적은 'F'","\n전체성적합:",total,"\n전체 성적합의 평균:",total5)
