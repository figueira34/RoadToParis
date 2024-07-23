import pandas as pd

brazil_boxscores = pd.read_csv('brazil_boxscores.csv')
france_boxscores = pd.read_csv('france_boxscores.csv')
germany_boxscores = pd.read_csv('germany_boxscores.csv')

boxscores = pd.concat([brazil_boxscores, france_boxscores, germany_boxscores], ignore_index=True)
boxscores.to_csv('boxscores.csv', index=False)
