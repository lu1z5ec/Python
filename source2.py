# input()함수를 사용하여 값 입력 받기

# int(정수형)으로 변환하지 않을경우 , 문자열로 인식하기 때문에 형 변환이 필요
num1 = int(input('입력1: '))
num2 = int(input('입력2: '))

result = num1+num2
print(num1,'+',num2,'=', result)

result = num1*num2
print(num1,'*',num2,'=',result)

result = num1/num2
print(num1,'/',num2,'=',result)

result = num1%num2
print(num1,'%',num2,'=',result)
