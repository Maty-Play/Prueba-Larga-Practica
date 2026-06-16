import os, time

producto = []

def limpiar():
    os.system("cls")

def pausar():
    time.sleep(2)

def validar_str(string):
    if len(string) > 0:
        return True
    else:
        print("El campo no puede vemor vacio")

def agregar_producto(producto):
    while True:
        nombre = input("Ingrese el nombre del producto: ").split()
        if validar_str(nombre):
            break
    
    while True:
        try:
            stock = int(input("Ingrese el numero: "))
            if validar_int(stock) == True:
                break
        except:
            print("El numero ingresado no es entero")
    
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if validar_rango_float(precio) == True:
                break
        except:
            print("El numero ingresado no es un entero")
    
    producto = {
        "Nombre": nombre,
        "Stock": stock,
        "Precio": precio,
        "Disponible": False
    }

def validar_int(numero):
    if numero > 0:
        return True
    else:
        print("el numero debe ser positivo")

def validar_rango_float(precio):
    if precio > 0:
        return True
    else:
        print("el numero debe ser mayor a 0")