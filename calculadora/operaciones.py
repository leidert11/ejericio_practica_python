# Crea un módulo llamado "operaciones" que contenga funciones para realizar operaciones
# matemáticas básicas, como suma, resta, multiplicación y división. Luego,
# crea un programa principal en otro archivo que importe el módulo y utilice esas
# funciones para realizar algunas operaciones.

from operator import  sub, mul, truediv

def suma():
    try:
        a=int(input("ingrese 1° numero : "))
        b=int(input("ingrese 2° numero : "))
        return a+b
    except ValueError:
        print("Error: Ingrese números válidos.")

def restar():
    try:
        a=int(input("ingrese 1° numero : "))
        b=int(input("ingrese 2° numero : "))
        return sub(a, b)
    except ValueError:
        print("Error: Ingrese números válidos.")

def multi():
    try:
        a=int(input("ingrese 1° numero : "))
        b=int(input("ingrese 2° numero : "))
        return mul(a,b)
    except ValueError:
        print("Error: Ingrese números válidos.")

def dividir():
    try:
        a=int(input("ingrese 1° numero : "))
        b=int(input("ingrese 2° numero : "))
        return truediv(a,b)
    except ValueError:
        print("Error: Ingrese números válidos.")