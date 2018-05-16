st=str(input("문자열 :"))
print("개별 문자 출력 :", st[0:len(st)])

for i in range(len(st)-1,-1,-1):
    print(st[i],end="")
    
