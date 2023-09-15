a = int(input())
b = int(input())
c = int(input())
discr = (b ** 2) - (4 * a * c)
if discr < 0:
    print('Нет корней')
if discr == 0:
    print(-(b / (2 * a)))
if discr > 0:
    x1 = ((-b + (discr ** (1 / 2))) / (2 * a))
    x2 = ((-b - (discr ** (1 / 2))) / (2 * a))
    print('Корни:', x1, ' ', x2)
