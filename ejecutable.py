import tableros as tab
import barcos 
import disparos as disp

#Creamos los tableros
tablero_A = tab.crea_tablero()
tablero_B = tab.crea_tablero()
tablero_a = tab.crea_tablero()
tablero_b = tab.crea_tablero()

#Colocamos los barcos
tablero_A = barcos.crear_y_colocar_los_barcos(tablero_A)
tablero_a = barcos.crear_y_colocar_los_barcos(tablero_a)

while True:
    accion = input(
        "Hola navegante, tienes tres opciones:" \
        "\n\t1.- Para disparar introduce las coordenadas escribiendo 'fila,columna'" \
        "\n\t2.- Enseñame mi tablero. Escribe 'mi tablero'" \
        "\n\t3.- Enseñame el tablero del rival. Escribe 'tablero rival'" \
        "\n\t4.- Para salir escribe 'salir'" \
        "\n"        
    )
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
        "Este es el tablero del PC: B",
        tablero_B,
        "(ocultar)Este es el tablero que ve el PC: a",
        tablero_a,
        "(ocultar)Este es tu tablero tal como lo ve el PC: b",
        tablero_b,
        sep="\n")
    else:
        try:
            x_str, y_str = accion.split(',')
            coordenada = (int(x_str),int(y_str))
            
            disp.disparo(tablero_a,tablero_B,coordenada)
            print("Así queda el tablero del rival:\n",tablero_B)

            disp.disparo_aleatorio(tablero_A,tablero_b)
            print("Así queda tu tablero:\n",tablero_A)

        except:
            print("algo salió mal, vuelve a intentarlo")            







