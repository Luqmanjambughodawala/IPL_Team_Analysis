import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("ipl.csv")
df.index = df.index + 1
df.drop(columns=["team1_players","team2_players"])
df["venue"] = df["venue"].str.split(",").str[0]
df["venue"] = df["venue"].str.replace(".", "", regex=False)

def selectTeam(team):
    new_df = df[(df["team1"] == team) | (df["team2"] == team)]
    new_df = new_df.drop(columns=["match_date","player_of_match","city","match_number","result","result_margin","target_runs","target_overs","super_over"])
    new_df["result"] = new_df["winner"].apply(lambda x: "won" if x == team else "lost")
    new_df = new_df.drop(columns = "winner")
    new_df["toss_result"] = new_df["toss_winner"].apply(lambda x: "won" if x == team else "lost")
    new_df = new_df.drop(columns = "toss_winner")
    total_games_played = len(new_df)
    print("---------------------Total games played till 2025---------------------")
    print(total_games_played)
    total_win = new_df.groupby("result").size()
    print("---------------------Total games won and lost till 2025--------------------- ")
    print(total_win)
    win_percent = (total_win.get("won", 0)/total_games_played)*100
    loss_percent = (total_win.get("lost", 0)/total_games_played)*100
    print("Win percentage = " , round(win_percent,2),"%")
    print("Loss percentage = " , round(loss_percent,2),"%")
    data = [total_win.get("won",0),total_win.get("lost", 0)]
    label = [f"win = {round(win_percent,2)}", f"loss {round(loss_percent,2)}"]
 
    total_toss_win = new_df.groupby("toss_result").size()
    print("---------------------Total toss won and lost till 2025---------------------")
    print(total_toss_win)
    toss_win_percent = (total_toss_win.get("won", 0)/total_games_played)*100
    toss_loss_percent = (total_toss_win.get("lost", 0)/total_games_played)*100
    print("Toss win percentage = " , round(toss_win_percent,2),"%")
    print("Toss loss percentage = " , round(toss_loss_percent,2),"%")
    data2 = [total_toss_win.get("won",0),total_toss_win.get("lost", 0)]
    label2 = [f"toss win = {round(toss_win_percent,2)}", f"toss loss {round(toss_loss_percent,2)}"]
    venue_games = new_df.groupby("venue").size()
    print("---------------------Games at each venue till 2025---------------------")
    print(venue_games)
    print("Most games at venue",venue_games.idxmax() ,venue_games.max())
    print("Least games at venue",venue_games.idxmax(), venue_games.min())
    plt.subplot(1,2,1)
    plt.pie(data, labels = label)
    plt.subplot(1,2,2)
    plt.pie(data2,labels=label2)
    plt.show()
    

 

selectTeam("Chennai Super Kings")
