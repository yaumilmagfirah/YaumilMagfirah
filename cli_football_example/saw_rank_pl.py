import pandas as pd
from models.players import Player


def get_top_five():
    players = Player.select()
    player_data = [
        (player.name, player.skill, player.pace, player.strength, player.age, player.cost)
        for player in players
    ]

    df = pd.DataFrame(player_data, columns=['Name', 'Skill', 'Pace', 'Strength', 'Age', 'Cost'])
    print(df)
    # Assign weights to each criterion (adjust weights as needed)
    weights = {'Skill': 0.3, 'Pace': 0.2, 'Strength': 0.15, 'Age': 0.15, 'Cost': 0.2}

    # Normalize the data (optional, if criteria have different scales)
    numeric_cols = df.select_dtypes(include=['number']).columns
    df_numeric = df[numeric_cols]
    print(numeric_cols)
    normalized_data = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())

    # axis=1 indicates that you want to perform the multiplication operation column-wise.
    # Calculate the weighted sum (WS)
    Weighted_Score = normalized_data.mul(weights, axis=1).sum(axis=1)

    # Rank the players based on the weighted score
    ranked_data = df.copy()
    ranked_data['Weighted_Score'] = Weighted_Score
    ranked_data = ranked_data.sort_values(by='Weighted_Score', ascending=False)

    print(ranked_data.head(5))

get_top_five()    