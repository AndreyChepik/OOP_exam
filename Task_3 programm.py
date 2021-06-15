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

    print(l)
    for elem in l.sort(reverse=False):
        if elem <10:
            m = elem

    return mult, m

print(funk())
