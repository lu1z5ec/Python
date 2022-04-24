#별칭 as 사용 
import turtle as t

t.shape('turtle')

#source4 비교 해보면 알겠지만, 같은 기능을 for반복문으로 쉽게 구현 한것 
for i in range(0,4):
    t.forward(200)
    t.right(90)

t.done()

