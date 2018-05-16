word=dict()
while True:
    eng=input("영어 단어 :")
    kor=input("한글 단어 :")
    if (eng=="") or (kor==""):
        break
    
    else:
        word[eng]=kor
print(word)
