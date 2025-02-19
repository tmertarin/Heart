import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

speed(0)
bgcolor('Black')
penup()
for i in range(0, 360, 1):  # 360 dereceyi 1'er birim artırarak gezelim.
    x = hearta(math.radians(i)) * 20  # Radyan kullanarak sinüs ve kosinüs hesaplaması.
    y = heartb(math.radians(i)) * 20
    goto(x, y)
    pendown()
    color("#F73487")
pendown()  # Çizim yapılmaya başlıyor
done()
