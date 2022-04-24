print("100") #문자
print("%d"%100) #숫자
print("%d %d" % (100,200)) 
print("%d"%(100+300))

print("\nㅡㅡㅡㅡㅡㅡㅡ마지막 출력 문자 지정ㅡㅡㅡㅡㅡㅡㅡㅡ")
print(1,2,end=' 마지막 출력 문자 지정')

print("\nㅡㅡㅡㅡㅡㅡㅡ출력형식 지정ㅡㅡㅡㅡㅡㅡㅡㅡ")
print(1,2,sep="/")

print("\nㅡㅡㅡㅡㅡㅡㅡ파일 객체로 출력ㅡㅡㅡㅡㅡㅡㅡㅡ")
f = open('text.txt','w')
print(1,2,3,4,5,file=f)
f.close()
open('text.txt').read()


