import pandas as pd

def main():
    #We load the data from the csv file in a variable to create a dataframe
    df_january = pd.read_csv("./Data/COVID_01-01-2021.csv")

    #Showing the general info of the dataframes
    print("Start of the program.")
    print("--------------------------------------------\n")
    print("Data frame information: \n")
    print(df_january.info())
    print("################################################\n")

    #Showing how much missing squares there are per column
    print("Empty boxes in each column: \n")
    print(df_january.isna().sum())
    print("################################################\n")

    #Showing the first 5 lines of the dataframe
    print("First five rows if the data frame: \n")
    print(df_january.head())
    print("################################################\n")

    #Showing the cases grouped by countries
    df_paises = df_january.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered", "Active"]].sum()
    print("COVID cases organized by countries (January 2021): \n")
    print(df_paises)
    print("################################################\n")

    #Sorting the cases by provinces/states and only taking the column for recovery
    df_provincias = df_january.groupby(["Province_State", "Country_Region"])["Recovered"].sum().reset_index()
    #Taking the provinces that has 0 recoveries
    provincias = df_provincias.loc[df_provincias["Recovered"] == 0]
    provincias = provincias.drop("Recovered", axis=1)
    print("List of provinces with no recoveries: \n")
    print(provincias)
    print("################################################\n")
    
    #Selecting the 10 countries that has the most active cases
    df_10_paises = df_paises.sort_values("Confirmed", ascending=False).head(10)
    print("Top 10 countries with more confirmed COVID cases (January 2021): \n")
    print(df_10_paises)
    print("################################################\n")
    print("--------------------------------------------\n")
    print("End of the program.")

main()