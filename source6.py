#원 그리기
import turtle as t

# 1. 바탕화면 색상 지정
t.bgcolor("yellow")

# 2. 펜 사이즈 지정
t.pensize(4)

# 3. 라인 색상 지정
t.color("green")

# 4. 펜 색상 지정
t.fillcolor("red")

# 5. 펜 그리기 시작
t.begin_fill()

# 6. 어떻게 그릴건지 circle(둥글게)
t.circle(100)

# 7. 그리기 종료
t.end_fill()

# 8. 그래픽 창이 열린 상태로 유지
t.done()