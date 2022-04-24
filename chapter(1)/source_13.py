print("%d"%123)
#오른쪽 5칸 확보후 출력 
print("%5d"%123)
#오른쪽 5칸 확보후 빈공간은 0으로 채움
print("%05d"%123)

print("%f"%3.14)
#오른쪽 7칸 확보후 반올림
print("%7.1f"%3.1415)
print("%7.3f"%3.1415)

print("%s"%"Python")
#오른쪽 10칸 확보
print("%10s"%"Python")



print("%d %5d %05d" % (123,456,789))
print("{0:d} {1:5d} {2:05d}".format(123,456,789))


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

print("%d %d %d" % (100,200,300))
print("x= %d y= %5d z=%05d"%(100,200,300))

#위치 인자
print("{0:d} {1:5d} {2:05d}".format(123,456,789))
print("{1:5d} {0:d} {2:05}".format(123,1234,1324))

#키워드 인자
print("{a} {b} {c} ".format(a=100, b= 200, c=300))

#문자열
print('{0} and "{1}"'.format("hello","world"))
print('i love {} for "{}"'.format("python","coding"))


