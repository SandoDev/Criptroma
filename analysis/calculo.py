"""Case 8"""
res = 0
for case8 in range(1, 0, -1):
    for case7 in range(case8, 0, -1):
        for case6 in range(case7, 0, -1):
            for case5 in range(case6, 0, -1):
                for case4 in range(case5, 0, -1):
                    for case3 in range(case4, 0, -1):
                        for case2 in range(case3, 0, -1):
                            # print(case2, " + ", res, " = ", case2 + res)
                            res = case2 + res
print(res)

"""Case 7"""
res = 0
for case7 in range(2, 0, -1):
    for case6 in range(case7, 0, -1):
        for case5 in range(case6, 0, -1):
            for case4 in range(case5, 0, -1):
                for case3 in range(case4, 0, -1):
                    for case2 in range(case3, 0, -1):
                        # print(case2, " + ", res, " = ", case2 + res)
                        res = case2 + res
print(res)

"""Case 6"""
res = 0
for case6 in range(3, 0, -1):
    for case5 in range(case6, 0, -1):
        for case4 in range(case5, 0, -1):
            for case3 in range(case4, 0, -1):
                for case2 in range(case3, 0, -1):
                    # print(case2, " + ", res, " = ", case2 + res)
                    res = case2 + res
print(res)

"""Case 5"""
res = 0
for case5 in range(4, 0, -1):
    for case4 in range(case5, 0, -1):
        for case3 in range(case4, 0, -1):
            for case2 in range(case3, 0, -1):
                # print(case2, " + ", res, " = ", case2 + res)
                res = case2 + res
print(res)

"""Case 4"""
print()
res = 0
for case4 in range(5, 0, -1):
    for case3 in range(case4, 0, -1):
        str_piramyd = ""
        for case2 in range(case3, 0, -1):
            str_piramyd = ""+str(case2)+" + "+str_piramyd
            print(str_piramyd)
            #print(case2, " + ", res, " = ", case2 + res)
            res = case2 + res
        #print()
    print()
print(res)


"""Case 3"""
res = 0
for case3 in range(6, 0, -1):
    for case2 in range(case3, 0, -1):
        # print(case2, " + ", res, " = ", case2 + res)
        res = case2 + res
print(res)

"""Case 2"""
res = 0
for case2 in range(7, 0, -1):
    # print(case2, " + ", res, " = ", case2 + res)
    res = case2 + res
print(res)


"""Case 1"""
res = 0
for case1 in range(8, 0, -1):
    res += 1
print(res)

"""Case 0"""
# cuando tiene 0 fragmentos
print(1)

"""
case-1:
    1 fragmento
    8 posiciones
    figuras posibles = 8

    haciendo sumatoria

    1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

case-2:
    2 fragmentos
    8 posiciones
    figuras posibles = 28

    cantidad de figuras posibles anteriores menos uno
    iterado la cantidad de figuras posibles menos uno
    haciendo sumatoria

    cada uno de los numero en esta piramide representa un elemento

    7 + 6 + 5 + 4 + 3 + 2 + 1
    6 + 5 + 4 + 3 + 2 + 1
    5 + 4 + 3 + 2 + 1
    4 + 3 + 2 + 1
    3 + 2 + 1
    2 + 1
    1

case-3:
    3 fragmentos
    8 posiciones
    figuras posibles = 56

    por cada elemento anterior menos uno
    iterar esa cantidad de veces y sumar

    6 + 5 + 4 + 3 + 2 + 1
    5 + 4 + 3 + 2 + 1
    4 + 3 + 2 + 1
    3 + 2 + 1
    2 + 1
    1

    5 + 4 + 3 + 2 + 1
    4 + 3 + 2 + 1
    3 + 2 + 1
    2 + 1
    1

    4 + 3 + 2 + 1
    3 + 2 + 1
    2 + 1
    1

    3 + 2 + 1
    2 + 1
    1

    2 + 1
    1

    1

case-4:
    4 fragmentos
    8 posiciones
    figuras posibles = 70

case-5:
    5 fragmentos
    8 posiciones
    figuras posibles = 56

case-6:
    6 fragmentos
    8 posiciones
    figuras posibles = 28

case-7:
    7 fragmentos
    8 posiciones
    figuras posibles = 8

case-8:
    8 fragmentos
    8 posiciones
    figuras posibles = 1
"""
