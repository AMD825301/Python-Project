def ddaAlgorithm(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        step = dx
    else:
        step = dy

    x_inc = dx / step
    y_inc = dy / step

    print("The points are: ")
    for i in range(0, step):
        x1 += x_inc
        y1 += y_inc
        print("({},{})".format(round(x1), round(y1)))


a = int(input("Enter the starting point, x1: "))
b = int(input("Enter the starting point, y1: "))
c = int(input("Enter the ending point, x2: "))
d = int(input("Enter the ending point, y2: "))

ddaAlgorithm(a, b, c, d)
