def funk():
    l = list()
    t = int(input("Введіть число"))
    l.append(t)
    while t<=20:
        t = int(input("Введіть число"))
        l.append(t)
    mult = 1
    for elem in l:
        mult *= elem

    l.sort()
    return mult, l.sort()

print(funk())
