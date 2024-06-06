import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #We load the data from the csv files in different variables to create multiple dataframes
    df_january = pd.read_csv("./Data/COVID_01-01-2021.csv")
    df_february = pd.read_csv("./Data/COVID_01-02-2021.csv")
    df_march = pd.read_csv("./Data/COVID_01-03-2021.csv")

    #We take Spain from every dataframe
    january = df_january.loc[df_january["Country_Region"] == "Spain"]
    january = january.groupby("Province_State")[["Confirmed", "Recovered"]].sum()
    february = df_february.loc[df_february["Country_Region"] == "Spain"]
    february = february.groupby("Province_State")[["Confirmed", "Recovered"]].sum()
    march = df_march.loc[df_march["Country_Region"] == "Spain"]
    march = march.groupby("Province_State")[["Confirmed", "Recovered"]].sum()

    """We concatenate the 3 dataframes"""
    spain = pd.concat([january, february, march], axis=1)
    """We create a MultiIndex to organize the data better"""
    idx = pd.MultiIndex.from_product([["January", "Feburary", "March"],
                                     ["Confirmed", "Recovered"]],
                                     names = ["months", "casos"])
    #We add the new index to the columns
    spain.columns = idx
    print(spain)

    #With the figure of pyplot and the library seaborn we show the results
    plt.figure(figsize=(14, 15))
    sns.heatmap(spain, annot=True, fmt=".2f", cmap="coolwarm", center=8, linewidths=.5).set(ylabel ="Provinces", xlabel="Month - Cases")

    plt.title("First quarter of COVID in Spain 2021", fontsize = 14)
    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=(.19))
    plt.show()

main()