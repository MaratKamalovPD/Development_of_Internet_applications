import sys
from math import sqrt

print(" Камалов М. Р. ИУ5-55Б")
if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
     print('Неверные параметры командной строки')
     exit()
elif len(sys.argv) != 1:
    print('Неверные параметры командной строки')
    exit()
else:
 while 1:
    try:
       a = float(input('Введите коэффициент a: '))
       break
    except:
        print("Коэффициент некорректен")
        print("попробуйте снова")
 while 1:
    try:
        b = float(input('Введите коэффициент b: '))
        break
    except:
        print("Коэффициент некорректен")
        print("попробуйте снова")
 while 1:
    try:
        c = float(input('Введите коэффициент c: '))
        break
    except:
        print("Коэффициент некорректен")
        print("попробуйте снова")

if a == 0 and b == 0 and c == 0:
    print("Х может быть любым")
    raise SystemExit
if a == 0 and b == 0 and c != 0:
    print("Уравнение не имеет корней")
    raise SystemExit
if (a == 0 and b != 0 and c == 0) or (a != 0 and b == 0 and c == 0):
    print("Х=0")
    raise SystemExit
if a == 0 and b != 0 and c != 0:
    try:
        print("X1=%s" % sqrt(-c/b))
        print("X2=%s" % -sqrt(-c/b))
    except:
         print("Уравнение не имеет решений")


if a != 0 and b == 0 and c != 0:
    try:
        print("X1=%s" % sqrt(sqrt(-c/a)))
        print("X2=%s" % -sqrt(sqrt(-c/a)))
    except:
         print("Уравнение не имеет решений")
    print("Х может быть любым")
if a != 0 and b != 0 and c == 0:
    print("Х1=0")
    if -b/a == 0:
        print("X2=%s" % sqrt(-b/a))
        print("X3=%s" % -sqrt(-b/a))
if a != 0 and b != 0 and c != 0:
    d = b * b - 4 * a * c
    if d < 0:
        print("Уравнение не имеет решений")
    else:
        if (-b+sqrt(d))/2*a > 0:
          print("X1=%s" % (sqrt((-b + sqrt(d))/2*a)))
          print("X2=%s" % -(sqrt((-b + sqrt(d))/2*a)))
          if (-b-sqrt(d))/2*a > 0:
             print("X3=%s" % (sqrt((-b - sqrt(d)) / 2 * a)))
             print("X4=%s" % -(sqrt((-b - sqrt(d)) / 2 * a)))
        else:
            if (-b - sqrt(d)) / 2 * a > 0:
                print("X1=" % (sqrt((-b - sqrt(d)) / 2 * a)))
                print("X2=" % -(sqrt((-b - sqrt(d)) / 2 * a)))
            else:
                print("Уравнение не имеет решений")