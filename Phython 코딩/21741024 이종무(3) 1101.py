#유원대 통합 정보 시스템 로그인 프로그램

id1 = "abcdefg"
pw = "1234"

def myf(uesr_id,uesr_pw) :
    if (id1 == uesr_id) & (pw == uesr_pw):
        return True
    else:
        return False

print("U1 Univercity student managment system")
uesr_id = input("put your ID")
uesr_pw = input("put your PASSWORD")

res = myf (uesr_id,uesr_pw)

while res == False:
    print("WORNG TRY AGAIN")
    uesr_id = input("put your ID")
    uesr_pw = input("put your PASSWORD")
    res = myf (uesr_id,uesr_pw)

print("LOGIN")
