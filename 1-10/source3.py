#더하기 / 함수 작성

#1. 함수 정의 (매개변수 a,b / 즉 2개의 값을 받아온 후 연산처리하여 결과값 반환)
def add(a,b):
    c= a+b
    return c

#2. 정의한 함수 인자값 전달후 , 함수측 에서 반환값이 있다면 sum변수에 저장
sum = add(1,2)

#3. sum변수 출력 / 3의 반환
print(sum)

#뺄셈
def minus (a,b):
    c = a-b
    return c
sum = minus(2,1)
print(sum)

#곱셈
def mul(a,b):
    c = a*b
    return c
sum = mul(2,2)
print(sum)

#나눗셈 (몫)
def divide(a,b):
    c = a/b
    return c
sum=divide(2,4)
print(sum)

#나눗셈 (나머지)
def divide(a,b):
    c = a%b
    return c
sum=divide(2,4)
print(sum)
