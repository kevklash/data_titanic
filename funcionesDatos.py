import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos y crear dataframe
df = pd.read_csv("data.csv")


def absluteV(pct, allvals):
    absolute = int(round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


# Buscar
def buscar(ticket: str):
    data = df.loc[df["Ticket"] == ticket]
    if len(data) == 0:
        print("No se encontraron resultados")
    else:
        for i, j in data.iterrows():
            print(i, j)
            print()

def bajas_pastel():
    # Otra manera para calcular bajas y sibrevivientes
    # bajas2 = df.groupby("Sobrevivió")['Sobrevivió'].count()
    # print(bajas2)

    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))
    sobrevivientes = len(df.loc[df["Sobrevivió"] == 1])
    bajas = len(df.loc[df["Sobrevivió"] == 0])
    labels = ["Sobrevivientes", "Bajas"]
    values = [sobrevivientes, bajas]
    wedges, texts, autotexts = ax.pie(values, autopct=lambda pct: absluteV(pct, values), textprops=dict(color="w"), explode=(0.02, 0.02))
    ax.legend(wedges, labels, title="Parametros", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=12, weight="bold")
    ax.set_title("Grafica de Bajas y Sobrevivientes")
    plt.show()

def sobrevivientesBarras():
    data = df.groupby("Clase")['Clase'].count()
    # print(data)
    data.plot(kind = "bar")
    plt.legend(title = "Grafica de Sobrevivientes por Clase")
    plt.xticks(rotation=0)
    plt.ylabel("# de Sobrevivientes")
    plt.show()

def costoTickets():
    filtro = df.loc[df["Tarifa"] != 0]
    print(f"El ticket más caro: $4{ filtro['Tarifa'].max() } ")
    print(f"El ticket más barato: ${ filtro['Tarifa'].min() } ")
