def filter_data_by_team(df, team):
    if 'TEAM' not in df.columns:
        raise KeyError("Expected column 'TEAM' not found in the data. Available columns: " + ", ".join(df.columns))

    return df[df['TEAM'] == team]

def calculate_top_scorers(df, top_n=10):
    df['PTS'] = pd.to_numeric(df['PTS'], errors='coerce')
    return df.nlargest(top_n, 'PTS')[['PLAYER', 'PTS', 'TEAM']]
