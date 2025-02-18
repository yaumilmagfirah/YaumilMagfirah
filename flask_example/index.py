from flask import Flask, render_template
import pandas as pd
from models.players import Player

app = Flask(__name__)

def WASPAS(data, weights, lambda_):
    """
    WASPAS method for football player transfer decision-making.

    Args:
        data: A pandas DataFrame containing player data and criteria.
        weights: A dictionary of weights for each criterion.
        lambda_: A weighting coefficient between 0 and 1.

    Returns:
        A pandas DataFrame with player rankings based on the WASPAS score.
    """
    # Normalize the data (min-max normalization)
    numeric_cols = data.select_dtypes(include=['number']).columns
    df_numeric = data[numeric_cols]
    normalized_data = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())

    # Calculate the weighted sum (WS)
    ws = normalized_data.mul(weights, axis=1).sum(axis=1)

    # Calculate the weighted product (WP)
    wp = normalized_data.pow(weights, axis=1).prod(axis=1)

    # Calculate the WASPAS score
    waspas_score = lambda_ * ws + (1 - lambda_) * wp

    # Rank the players based on the WASPAS score
    ranked_data = data.copy()
    ranked_data['WASPAS_Score'] = waspas_score
    ranked_data = ranked_data.sort_values(by='WASPAS_Score', ascending=False)

    return ranked_data

def get_top_five():
    players = Player.select()
    player_data = [
        (player.name, player.skill, player.pace, player.strength, player.age, player.cost)
        for player in players
    ]

    data = pd.DataFrame(player_data, columns=['Name', 'Skill', 'Pace', 'Strength', 'Age', 'Cost'])

    # Assign weights to criteria
    weights = {'Skill': 0.3, 'Pace': 0.2, 'Strength': 0.15, 'Age': 0.15, 'Cost': 0.2}

    # Set the weighting coefficient (lambda)
    lambda_ = 0.5

    # Apply WASPAS
    ranked_df = WASPAS(data, weights, lambda_)

    return ranked_df.head(5)

@app.route('/')
def index():
    top_players = get_top_five()
    return render_template('index.html', players=top_players)

if __name__ == '__main__':
    app.run(debug=True)
