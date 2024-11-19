def filter_data_by_team(df, team):
    return df[df['TEAM'] == team]

def calculate_top_scorers(df, top_n=10):
    df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
    return df.nlargest(top_n, 'PTS')[['PLAYER', 'PTS', 'TEAM']]
