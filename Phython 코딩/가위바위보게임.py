# 가위바위보

import random

# 답변을 입력해봅시다.
ans1="가위"
ans2="바위"
ans3="보"
ans4="가위"
ans5="바위"
ans6="보"
ans7="가위"
ans8="바위"
ans9="보"
ans10="가위"
ans11="바위"
asn12="보"
ans13="가위"
ans14="바위"
ans15="보"
ans16="가위"
ans17="바위"
ans18="보"
ans19="가위"
ans20="바위"
ans21="보"
print("가위바위보에 오신 것을 환영합니다.")
#사용자의 질문을 입력 받습니다.
question = input("\n")
print("가위바위보...\n" * 4)
#질문에 알맞는 답변을 하는 일에 raindint() 함수를 활용합니다.
choice=random.randint(1,21)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
elif choice==8:
    answer=ans8
elif choice==9:
    answer=ans9
elif choice==10:
    answer=ans10
elif choice==11:
    answer=ans11
elif choice==12:
    answer=ans12
elif choice==13:
    answer=ans13
elif choice==14:
    answer=ans14
elif choice==15:
    answer=ans15
elif choice==16:
    answer=ans16
elif choice==17:
    answer=ans17
elif choice==18:
    answer=ans18
elif choice==19:
    answer=ans19
elif choice==20:
    answer=ans20
else:
    answer=ans21

# 화면에 답변을 출력합니다.
print(answer)

input("\n\n마치려면 엔터키를 누르세요.")
