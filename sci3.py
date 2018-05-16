score=int(input("점수 :"))

if score >=0 and score<=100:

    if score >=90 :

        print(score,": A")

    elif score >=80 and score<=70 :

        print(score,": B")

    elif score >=70 and score<=60 :

        print(score,": C")

    else:

        print(score,": F")

 

else:

    print("점수 :",score)

    print("입력 가능한 점수 범위는 0~100입니다.")

 
