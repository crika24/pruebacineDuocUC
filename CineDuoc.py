asientos=[[".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]

def imprimir():
    for filas in asientos:
        for columnas in filas:
            print(columnas, end=" ")
        print()
print("*********Bienvenido a CineDuoc.**********")
entrada=2500
while True:    
    try:
        op=int(input("Ingrese una opcion: \n 1) Si desea ver la pelicula -Spiderman 1- \n 2) Buscar asiento \n 3) Imprimir Boleta \n 4) Salir \n:"))
        if op==1:
            print("*****Estos son los asientos disponibles*****")
            imprimir()
            print("indiqueme el asiento que desea \n NOTA: \n fila (Izquierda a Derecha)\n Columna vertical  (Arriba hacia Abajo)")
            fila=int(input("Ingrese Fila: "))
            columna=int(input("Ingrese Columna: "))
            asientos[fila][columna]="x"
            imprimir()
            nombre=input("Ingrese su nombre: ").lower()
            while True:
                try:
                    estudiante=int(input(f"Señor {nombre} Pertenece a DuocUC: \n1) SI \n2) NO \n:"))
                    if estudiante==1:
                        descuento=entrada*0.20
                    else:
                        descuento=0
                        print("No pertenece a DuocUC, No tiene descuento")
                    break
                except:
                    print("ingrese una opcion valida")
        elif op==2:
            preg_nombre=input("Ingrese su nombre: ").lower()
            preg_nombre.lower
            if preg_nombre==nombre:
                print("Usted ya posee un asiento")
                imprimir()
            else:
                print("Usted no posee ningun asiento, por favor compre uno")
        elif op==3:
            print("***********************************")
            print("**************BOLETA***************")
            print("***********************************")
            print("Nombre pelicula: Spiderman 1")
            print("Nombre del comprador:",nombre)
            print("Asiento:")
            imprimir()
            print("Descuento:",descuento)
            print("Total:", entrada-descuento)
            print("***********************************")
            print("***********************************")
            print("***********************************")
        elif op==4:
            break
    except:
        print("ingrese una opcion valida")
        