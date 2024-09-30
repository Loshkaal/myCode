import math

x = float(input())
y = float(input())
gip_1 = (x ** 2) + (y ** 2)
gip = math.sqrt(gip_1) #  гип рандомной точки
gip_circle = float(10) # гип зеленой зоны
gip_danger = float(5) #гип запрещенной зоны
y_parab = (0.25 * (x ** 2)) + (0.5 * x) + 8.75
if  gip > gip_circle:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
elif x >= 0 and y >= 0:
    if gip <= gip_danger:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x <= 0 and y >= 0:
    if x < -4 or x == -4 and x > -7 or x == -7 and y >= 0:
        t_0 = math.atan(5/3) # тан красного треугольника
        arc_t = math.atan(y/(math.fabs(-7) - math.fabs(x))) #  тан точки которую ищем 
        if arc_t <= t_0:
            print("Опасность! Покиньте зону как можно скорее!")
        else:
             print("Зона безопасна. Продолжайте работу.")
    elif x <= 0 and x >= -4 and y >= 0 and y <= 5:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif (x >= 0 and y <= 0) or (x <= 0 and y <= 0):  
    if y < y_parab:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x == 0 and y == 0:
    print("Опасность! Покиньте зону как можно скорее!")




