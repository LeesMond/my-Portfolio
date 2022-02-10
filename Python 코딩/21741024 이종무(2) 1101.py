#게임 비밀번호 프로그램
m1 = "1234"
def tf (pas,m1):
    if pas == m1:
        return True
    else:
        return False

print("HELLO")
pas = input("put your password")



#참 거짓 판별
res = tf(pas,m1)

while res == False:
    print("no match try again")
    pas = input("try again")
    res = tf(pas,m1)

print("OPEN")
