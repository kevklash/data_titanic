import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def limpiar_crear(df):
    # Rellenamos datos incompletos
    df_lleno = df.fillna({"Edad": 0,
                          "Ticket": "Desconocido",
                          "Tarifa": 0,
                          "Cabina": "Desconocida",
                          "Bote de Rescate": "Desconocido",
                          "Cuerpo": "Desconocido",
                          "Destino": "Desconocido"})

    # Convertimos a número los datos relevantes
    df_lleno[["Edad", "Tarifa"]] = df_lleno[["Edad", "Tarifa"]].apply(np.floor)
    # Alt: df_lleno["column"].apply(pd.to_numeric)

    # Convertimos a string los codigos de ticket
    df_lleno[["Ticket"]] = df_lleno[["Ticket"]].astype(str)

    # Exportamos a nuevo archivo de datos con data limpia
    df_lleno.to_csv("data.csv")

def removerNA(df):
    df_lleno = df.dropna()
    return df_lleno