import pandas as pd
from models.players import Player 
df = pd.read_csv('./db/players.csv')

for index, row in df.iterrows():
    Player.create(
        name=row['Player'],
        skill=row['Skill'],
        pace=row['Pace'],
        strength=row['Strength'],
        age=row['Age'],
        cost=row['Cost']
    )