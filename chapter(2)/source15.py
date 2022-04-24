#format 대신 f-string활용

#f-string
str = 'str'
print(f'a is {str}')

#format 
print("a is {0}".format("format"))

x,y,z= 1,2,3
print(f'a is {x},{y},{z}')

print("a is {x}, {y}, {z}".format(x=10,y=20,z=30))

name = 'index'
age = 99
print(f'My Name is {name} And My Age {age}')

print("My Name Is {0} And My Age {1}".format("index",99))



#줄이 길어질 경우 출력 결과 예측
print("hello world")
print('\Hello world')

print("I don't Know ")
print('I dont \t know')

print("""\
line1
line2
line3\
""")

print("""aaaaaaaaaaaaaaaaa""")