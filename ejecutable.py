from funciones import tableros as tab
from funciones import barcos 
from funciones import disparos as disp

#Creamos los tableros
tablero_A = tab.crea_tablero()
tablero_B = tab.crea_tablero()
tablero_a = tab.crea_tablero()
tablero_b = tab.crea_tablero()

#Colocamos los barcos
tablero_A = barcos.crear_y_colocar_los_barcos(tablero_A)
tablero_a = barcos.crear_y_colocar_los_barcos(tablero_a)

#Mensaje de bienvenida
print("*"*20,"\nHola navegante, vamos a jugar a hundir la flota.")

#Empieza el turno de disparos
while True:
    accion = input(
        "********************"\
        "\n\tEs tu turno.Tienes tres opciones:" \
        "\n\t1.- Para disparar introduce las coordenadas escribiendo 'fila,columna'" \
        "\n\t2.- Enseñame mi tablero. Escribe 'mi tablero'" \
        "\n\t3.- Enseñame el tablero del rival. Escribe 'tablero rival'" \
        "\n\t4.- Para salir escribe 'salir'" \
        "\n")
    if accion == "salir":
        print("Gracias por jugar. ¡Hasta pronto!")
        exit()
    elif accion == "mi tablero":
        print(tablero_A)
    elif accion == "tablero rival":
        print(tablero_B)
    elif accion == "trampas":
        print(
        "Este es tu tablero: A",
        tablero_A,
        "(oculto)Este es el tablero del PC: a",
        tablero_a,
        "Así ves el tablero del PC: B",
        tablero_B,
        "(oculto)Este es tu tablero tal como lo ve el PC: b",
        tablero_b,
        sep="\n")
    else:
        try:
            x_str, y_str = accion.split(',')
            coordenada = (int(y_str),int(x_str))
            
            if coordenada[0] > 9 or coordenada[0] < 0 \
                or coordenada[1] > 9 or coordenada[1] < 0:
                print("Las coordenadas deben estar entre 0,0 y 9,9")
                continue

            if tablero_a[coordenada] == "X" or tablero_a[coordenada] == "~":
                print("Ya has disparado a esa posición, dispara a otro sitio")
                continue
                        
            else:
                disp.disparo(tablero_a,tablero_B,coordenada)
                print("Así queda el tablero del rival:\n",tablero_B)
            
                if tablero_a[coordenada] == "X":
                    print("Vuelve a ser tu turno")
                    continue

            print("Es el turno del rival")
            disp.disparo_aleatorio(tablero_A,tablero_b)
            print("Así queda tu tablero:\n",tablero_A)

        except:
            print("Algo salió mal, vuelve a intentarlo")   
            continue         







