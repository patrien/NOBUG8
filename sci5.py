s=0
items={"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}

while True:
    it=str(input("제품명 :"))
    if it in items:
        s=s+items[it]
        print("[%s:%d]>%d"%(it,items[it],s))
    elif it=="":
        break
        
    else:
        print(it,"는 미등록 제품입니다.")

    
print("총 금액 :",s)
    
        
        
