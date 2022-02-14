import cProfile
def a():
    class rectangulo:
        pass

    p = rectangulo()
    p.base = int(input("Ingrese su base "))
    p.altura = int(input("Ingrese su altura "))

    area = p.base * p.altura


    print (area)
cProfile.run('a()')