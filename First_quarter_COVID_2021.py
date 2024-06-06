import pandas as pd
import matplotlib.pyplot as plt

def main():
    #We load the data from the csv files in different variables to create multiple dataframes
    df_january = pd.read_csv("./Data/COVID_01-01-2021.csv")
    df_february = pd.read_csv("./Data/COVID_01-02-2021.csv")
    df_march = pd.read_csv("./Data/COVID_01-03-2021.csv")

    january = df_january.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum()
    february = df_february.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum()
    march = df_march.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum()

   #We make 3 list out of each dataframe to have a list with each data per month
    confirmed = [january["Confirmed"].sum(), february["Confirmed"].sum(), march["Confirmed"].sum()]
    deaths = [january["Deaths"].sum(), february["Deaths"].sum(), march["Deaths"].sum()]
    recovered = [january["Recovered"].sum(), february["Recovered"].sum(), march["Recovered"].sum()]
    #We make another list with the monts
    month = ["January", "February", "March"]
    #We finally create a new dataframe with all the others
    trimestre = pd.DataFrame(
        {"Months": month, 
        "Confirmed": confirmed, 
        "Deaths": deaths, 
        "Recovered": recovered})
    
    #We use pyplot to graphic
    with plt.style.context("seaborn-v0_8-darkgrid"):
        fig, eje = plt.subplots(figsize=(8, 9))
        
        eje.plot(trimestre.Months, trimestre.Confirmed, marker = 'o', color = 'b', label= 'Confirmed')
        eje.plot(trimestre.Months, trimestre.Deaths, marker = 'o', color = 'r', label= 'Deaths')
        eje.plot(trimestre.Months, trimestre.Recovered, marker = 'o', color = 'g', label= 'Recovered')
    
    
    eje.set(xlabel="Months", ylabel="Cases", title="Evolution of COVID in first quarter 2021")
    eje.legend(bbox_to_anchor=(1, 1))
    plt.subplots_adjust(right=(.78))
    plt.show()


main()