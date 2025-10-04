accion = input()

x_str, y_str = accion.split(',')
coordenada = (int(x_str),int(y_str))
print(coordenada)
print(type(coordenada[0]))
print(type(coordenada[1]))