import matplotlib.pyplot as plt

def plot_top_scorers(df):
    players = df['PLAYER']
    points = df['PTS']

    plt.figure(figsize=(10, 6))
    plt.bar(players, points)
    plt.title("Top Scorers in NBA")
    plt.xlabel("Players")
    plt.ylabel("Points")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
