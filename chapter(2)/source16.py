#각 변수 0으로 초기화
res1,res2,res3,res4 = 0,0,0,0
num = 0
num = int(input("교환할 돈은 얼마? : "))

#// : 몫 (소수점 버리고 값 변수에 대입), % : 나머지
#반면 / 같은 경우 나눈값을 그냥 변수에 대입
res1 = num // 500
num %=500

res2 = num // 100
num %= 100

res3 = num // 50
num %= 50

res4 = num // 10
num%=10

print("500원짜리 ==>>", res1)
print("100원짜리 ==>>", res2)
print("50원짜리 ==>>", res3)
print("10원짜리 ==>>", res4)
print("바꾸지 못한 잔돈 : %d"%num)

