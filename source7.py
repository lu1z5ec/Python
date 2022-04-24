import turtle as t
# 거북이 모양
t.shape('turtle')
# 라인 색
t.color("green")
# 속도
t.speed(999)

#데이터 사용자로 부터 입력 받아옴
r = int(input("몇개를 그릴까요? : "))

# 0~입력받은값 만큼 그려짐
for i in range(r):
    # 원 모양 / 그려질 각도 / 20씩 이동
    t.circle(100)
    t.right(360/r)
    t.forward(20)
    
t.done()
