#현관문 비번 프로그램

#기계 비밀번호를 초기화
m1 = "1234"

#참 거짓 판별
def tf (pw,m1):
    if pw == m1:
        return True
    else:
        return False
#기계에 저장된 비밀번호와 내가 입력한 비밀번호 비교
pw = input("비번 입력")
#같으면 OPEN 다르면 CLOSE

res = tf(pw,m1)

while res == False:
    print("no match try again")
    pw = input("try again")
    res = tf(pw,m1)

print("OPEN")
