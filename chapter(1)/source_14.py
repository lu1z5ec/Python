#변수 선언방법
#불린, 정수, 실수, 문자열
boolvar=True
num=10
floatnum=3.14
str="Hello World"


#type()함수를 이용하여 해당 변수가 어떠한 타입인지 알수 있다.
type(boolvar),type(num),type(floatnum),type(str)


#
def myfunc():
    print("call back")

globalnum = 100

if __name__ == '__main__':
    print("main 함수 부분 실행")
    myfunc()
    print("%d"%(globalnum))