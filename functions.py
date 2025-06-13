
def agregar_nota (lista_notas,a):
    nota_estudiante = 0
    while nota_estudiante <= 0.9 or nota_estudiante > 7:
        try:
            nota_estudiante = float(input(f"{a} Ingrese la nota del estudiante (valores entre 1.0 y 7.0):\n"))
        except:
            print(f"{a} Ingrese solo numeros {a}\n")
    print (f"Nota guardada con exito {a}\n")
    lista_notas.append(nota_estudiante)

def mostrar_notas (lista_notas,a):
    if len(lista_notas) == 0:
        print (f"\n No hay notas por mostrar {a}\n")
    else:
        i = 0
        for nota in lista_notas:
            i += 1 #Contador de ingreso de notas
            print (f"Nota Nro.{i}: {nota}")
            
def calcular_promedio (lista_notas,a):
    promedio = f"\t No hay notas para generar un promedio {a}\n"
    if len(lista_notas) == 0:
        print (promedio)
    else:
        x = 0 #Contador de notas
        total = 0 # Acumulador de notas
        for nota in lista_notas:
            x += 1
            total += nota
        promedio = total / x
        print(f"El promedio de notas ingresadas es {round(promedio, 2)}\n")

def mostrar_max_min (lista_notas,a):
    if len(lista_notas) == 0:
        print ("""\t No hay suficientes datos
         para generar maximo y minimo\n""")
    else:
        nota_max = max(lista_notas)
        nota_min = min(lista_notas)
        print(f"""{a} NOTA MAXIMA: {nota_max}\n
{a} NOTA MINIMA: {nota_min}\n""")

def salida(a):
    print (f"{a} El programa se ha cerrado con exito {a}")
    return False

def menu (a):
    on = True
    lista_notas = []
    while on:
        print (f"""\t\t MENU DEL PROFE {a}\n
        1) Ingresar las notas de los estudiantes
        2) Mostrar todas las notas ingresadas
        3) Calcular el promedio de las notas
        4) Mostrar la nota más alta y la nota más baja
        5) Salir del programa\n""")
        try:
            opcion = int(input(f"\t{a} Seleccione una opcion:\n"))
            if opcion == 1:
                agregar_nota (lista_notas,a)
            elif opcion == 2:
                mostrar_notas (lista_notas,a)
            elif opcion == 3:
                calcular_promedio (lista_notas,a)
            elif opcion == 4:
                mostrar_max_min (lista_notas,a)
            elif opcion == 5:
                on = salida(a)
            else:
                print (f"\t Ingrese solo opciones validad (1,2,3,4 o 5){a}\n")  
        except:
            print (f"\t Ingrese un caracter numerico entero por favor {a}\n")
        
