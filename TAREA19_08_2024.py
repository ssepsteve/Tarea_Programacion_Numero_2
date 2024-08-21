def problema1(diccionario):
    listaValoresDiccionario = [diccionario[i] for i in diccionario]
    listaValoresDiccionarioTipos = [type(i) for i in listaValoresDiccionario]
    if type(1) in listaValoresDiccionarioTipos and (type("str") not in listaValoresDiccionarioTipos or type(False) not in listaValoresDiccionarioTipos):
        listaValoresDiccionario.sort()
        print(f"Lista valores de manera ascendente: {listaValoresDiccionario}")
    elif type("str") in listaValoresDiccionarioTipos and (type(1) not in listaValoresDiccionarioTipos or type(False) not in listaValoresDiccionarioTipos):
        listaValoresDiccionario.sort()
        print(f"Lista valores de manera ascendente: {listaValoresDiccionario}")
    elif type(False) in listaValoresDiccionarioTipos and (type(1) not in listaValoresDiccionarioTipos or type("str") not in listaValoresDiccionarioTipos):
        listaValoresDiccionario.sort()
        print(f"Lista valores de manera ascendente: {listaValoresDiccionario}")
    else:
        print("Los datos del diccionario no son del mismo tipo")


def problema2(diccionario1,diccionario2):
    diccionarioCompartido = {}
    if len(diccionario1) == len(diccionario2):
        for i,j in zip(diccionario1,diccionario2):
            if i in diccionario2:
                if diccionario1[i] in diccionario2[i]:
                    pass
            else:
                return False
    return True



def problema3(diccionario1,diccionario2):
    diccionarioNuevo = {}
    for i in diccionario1:
        if i in diccionario2:
            diccionarioNuevo[i] = diccionario1[i]
        if i not in diccionario2:
            diccionarioNuevo[i] = diccionario1[i]
    for j in diccionario2:
        if j not in diccionario1:
            diccionarioNuevo[j] = diccionario2[j]
    return diccionarioNuevo

def problema4(listaNombres,listaApellidos,listaEdad):
    diccionarioPersona = {}
    if len(listaNombres) == len(listaApellidos) and len(listaNombres) == len(listaEdad):
        for i in range(len(listaNombres)):
            diccionarioPersona["nombre"] = listaNombres[i]
            diccionarioPersona["apellido"] = listaApellidos[i]
            diccionarioPersona["edad"] = listaEdad[i]
            print(diccionarioPersona)
            diccionarioPersona = {}
    else:
        print("Faltan datos")

if __name__ == "__main__":
    print("Problema 1")
    diccionarioProblema1Caso1 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    print(f"Caso 1: Diccionario con solo valores de strings, diccionario: {diccionarioProblema1Caso1}")
    problema1(diccionarioProblema1Caso1)

    diccionarioProblema1Caso2 = {1:3,4:2,6:1,7:9}
    print(f"Caso 2: Diccionario con solo valores enteros, diccionario: {diccionarioProblema1Caso2}")
    problema1(diccionarioProblema1Caso2)

    diccionarioProblema1Caso3 = {1:False,4:True,6:False,7:True}
    print(f"Caso 3: Diccionario con solo valores booleanos, diccionario: {diccionarioProblema1Caso3}")
    problema1(diccionarioProblema1Caso3)

    diccionarioProblema1Caso4 = {1:False,4:"string",6:7,7:9.8}
    print(f"Caso 4: Diccionario con diferentes valores, diccionario: {diccionarioProblema1Caso4}")
    problema1(diccionarioProblema1Caso4)

    print("Problema 2")
    diccionario1Problema2Caso1 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    diccionario2Problema2Caso1 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    print(f"Caso 1: Diccionarios Con mismas claves y valores, diccionario1: {diccionario1Problema2Caso1},diccionario2: {diccionario2Problema2Caso1}")
    print(problema2(diccionario1Problema2Caso1,diccionario2Problema2Caso1))

    diccionario1Problema2Caso2 = {"Hola":"Hola","abc":"Abc","Dios":"Dios"}
    diccionario2Problema2Caso2 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    print(f"Caso 2: Diccionarios Con diferentes claves y valores, diccionario1: {diccionario1Problema2Caso2},diccionario2: {diccionario2Problema2Caso2}")
    print(problema2(diccionario1Problema2Caso2,diccionario2Problema2Caso2))

    print("Problema 3")
    diccionario1Problema3Caso1 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    diccionario2Problema3Caso1 = {1:3,4:2,6:1,7:9}
    print(f"Caso 1: Diccionarios Diferentes , diccionario1: {diccionario1Problema3Caso1}, diccionario2:{diccionario2Problema3Caso1}")
    print(problema3(diccionario1Problema3Caso1,diccionario2Problema3Caso1))

    diccionario1Problema3Caso2 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    diccionario2Problema3Caso2 = {1:3,"Abc":"xyz",6:1,7:9}
    print(f"Caso 2: Diccionarios con una llave compartida: {diccionario1Problema3Caso2}, diccionario2:{diccionario2Problema3Caso2}")
    print(problema3(diccionario1Problema3Caso2,diccionario2Problema3Caso2))

    diccionario1Problema3Caso3 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    diccionario2Problema3Caso3 = {"Hola":"Hola","Abc":"Abc","Dios":"Dios"}
    print(f"Caso 2: Diccionarios iguales: {diccionario1Problema3Caso3}, diccionario2:{diccionario2Problema3Caso3}")
    print(problema3(diccionario1Problema3Caso3,diccionario2Problema3Caso3))

    print("Problema 4")
    listaNombresCaso1 = ["Juanito","Pablo","Sebastian"]
    listaApellidosCaso1 = ["Perez","Hernandez","Espitia"]
    listaEdadCaso1 = [12,43,56]
    print(f"Caso 1: Listas Completas, listaNombres:{listaNombresCaso1},listaApellidos:{listaApellidosCaso1},listaEdad:{listaEdadCaso1}")
    problema4(listaNombresCaso1,listaApellidosCaso1,listaEdadCaso1)
    
    print(f"Caso 2: Listas Incompletas, listaNombres:{listaNombresCaso1},listaApellidos:{listaApellidosCaso1},listaEdad:{listaEdadCaso1}")
    listaNombresCaso2 = ["Juanito","Pablo"]
    listaApellidosCaso2 = ["Perez","Hernandez","Espitia"]
    listaEdadCaso2 = [12,43,56]
    print(f"Caso 1: Listas Completas, listaNombres:{listaNombresCaso2},listaApellidos:{listaApellidosCaso2},listaEdad:{listaEdadCaso2}")
    problema4(listaNombresCaso2,listaApellidosCaso2,listaEdadCaso2)