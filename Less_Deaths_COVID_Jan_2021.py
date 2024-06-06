import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #We load the data from the csv file in a variable to create a dataframe
    df_january = pd.read_csv("./Data/COVID_01-01-2021.csv")
    df_paises = df_january.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum()
    df_paises.to_csv("Cases by country.csv")
    #We take only the countries that has less than 150 deaths
    df_paises = df_paises.loc[df_paises["Deaths"] < 150]

    #Showing the results with a graphic
    with sns.color_palette("bright6", 3): df_paises.plot(kind="bar", stacked=True, figsize=(10, 10))
    plt.xticks(rotation=90)
    plt.xticks(fontsize=8)
    #Le asignamos una etiqueta al eje X
    plt.xlabel("Countries")
    #Ajustamos el límite inferior para que se vea bien al momento de abrir la gráfica
    plt.subplots_adjust(bottom=(.28))
    #Finalmente mostramos el resultado con pyplot
    plt.show()

main()