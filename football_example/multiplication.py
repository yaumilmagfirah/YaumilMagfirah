import pandas as pd
from models.players import Player

players = Player.select()
player_data = [
    (player.name, player.skill, player.pace, player.strength, player.age, player.cost)
    for player in players
]

df = pd.DataFrame(player_data, columns=['Name', 'Skill', 'Pace', 'Strength', 'Age', 'Cost'])
numeric_cols = df.select_dtypes(include=['number']).columns
df_numeric = df[numeric_cols]
print('players matrix')
print(df_numeric.head(2))
# Weights
weights = {'Skill': 0.3, 'Pace': 0.2, 'Strength': 0.15, 'Age': 0.15,'Cost':0.2}

print('weight matrix')
print(weights)

# Multiplication with axis=1
result_mul = df_numeric.mul(weights, axis=1)

print('result multiplication')
print(result_mul.head(2))

result_sum = result_mul.sum(axis=1)

print('SUM of (Multiplication Weight and Attributes)')
print(result_sum.head(2))