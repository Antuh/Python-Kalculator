print ("*" * 10, "Консольныйалькулятор", "*" * 10)
while True:
    print ("Введите q для выхода")
    s = input("Операция (+,-,*,/,^,%,корень) ")
    if s == "q": break
    if s in ("+","-","*","/","^","%","корень"):
        x = float(input("x="))
        y = float(input("y="))
        if s == "+":
            print("%.2f" % (x+y))
        elif s == "-":
            print("%.2f" % (x-y))
        elif s == "*":
            print("%.2f" % (x*y))
        elif s == "^":
            print("%.2f" % (x**y))
        elif s == "/":
            try:
                print("%.2f" % (x/y))
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
        elif s == "%":
            print("%.2f" % (x*(y/100)))
        elif s == "корень":
            if y == 0:
                print("Нет такого корня!")
            else:
                from decimal import *
                getcontext().prec = 3
                print(Decimal(x)**Decimal(1/y))
    else:
        print("Неверный знак")