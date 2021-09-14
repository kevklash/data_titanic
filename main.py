import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Importamos funcion donde limpiamos nuestra data y creamos un nuevo csv
from limpieza import limpiar_crear
# Importamos nuestras funcionoes
from funcionesDatos import buscar, bajas_pastel, sobrevivientesBarras, costoTickets
import os


if __name__ == '__main__':
    # Llamamos la funcion para limpiar y crear un nuevo csv
    # df_raw = pd.read_excel("lista.xlsx")
    # limpiar_crear(df_raw) # retornamos y cramos data.csv

    while True:
        os.system("cls")  # Limpieza de pantalla
        print("Menu:")
        print("1. Buscar un pasajero por codigo de ticket")
        print("2. Gráfica de bajas y sobrevivientes(pastel)")
        print("3. Gráfica de sobrevivientes por clase(barras)")
        print("4. Reporte de costos de tickets")
        print("5. Salir")

        opc = input("Seleccione su opción: ")

        if opc == "1":
            ticket = input("Digite el codigo del ticket(Ej: PC 17318 o 113781): ")  # Capturando el ticket
            buscar(ticket)
            input()

        elif opc == "2":
            bajas_pastel()
            input()

        elif opc == "3":
            sobrevivientesBarras()
            input()

        elif opc == "4":
            costoTickets()
            input()

        elif opc == "5":
            print("Hasta pronto...")
            input()
            break

        else:
            print("Opción incorrecta")
            input()
            continue