def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

import math

def move(x,y,step,angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)

#一元二次方程求解
def quadratic(a,b,c):
    sac = b*b - 4*a*c
    if sac < 0:
        print('无解')
        return
    else:
        x1 = (0-b + math.sqrt(sac))/(2*a)
        x2 = (0-b - math.sqrt(sac))/(2*a)
        return x1,x2

print(quadratic(2,3,1))