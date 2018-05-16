word=dict()
while True:
    
    eng=input("영어 단어 :")
    if (eng==""):
        break
    if len(word)==0:
         print("사전이 비어 있습니다.")
         print("단어를 추가 합니다.")
         kor=input("한글 단어 :")
         word[eng]=kor
    else:
        if eng in word:
            print("한글 단어 :",word[eng])
        else:
            print(eng,"단어가 등록되어있지 않습니다.")
            print("단어를 추가 합니다.")
            kor=input("한글 단어 :")
            word[eng]=kor
        
print(word)
