import pandas as pd

def main():
    #We load the data from the csv files in different variables to creat the dataframes
    df_enero = pd.read_csv("./Data/COVID_01-01-2021.csv")

    #Showing the general info of the dataframes
    print("Inicio del programa.")
    print("--------------------------------------------\n")
    print("Información del data frame: \n")
    print(df_enero.info())
    print("################################################\n")

    #Showing how much missing squares there are per column
    print("Casillas vacías en cada columna: ")
    print(df_enero.isna().sum())
    print("################################################\n")

    #Showing the first 5 lines of the dataframe
    print("Cinco primeras líneas del data frame: \n")
    print(df_enero.head())

    #Showing the cases grouped by countries
    df_paises = df_enero.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered", "Active"]].sum()
    print("Casos COVID organizados por países (Enero 2021): \n")
    print(df_paises)

    #Sorting the cases by provinces/states and only taking the column for recovery
    df_provincias = df_enero.groupby(["Province_State", "Country_Region"])["Recovered"].sum().reset_index()
    #Taking the provinces that has 0 recoveries
    provincias = df_provincias.loc[df_provincias["Recovered"] == 0]
    provincias = provincias.drop("Recovered", axis=1)
    print(provincias)
    
    #Selecting the 10 countries that has the most active cases
    df_10_paises = df_paises.sort_values("Confirmed", ascending=False).head(10)
    print("10 países con más casos COVID confirmados (Enero 2021): \n")
    print(df_10_paises)

main()