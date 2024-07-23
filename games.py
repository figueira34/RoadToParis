import pandas as pd

data = {
    'DATE': ['02/07/2024', '04/07/2024', '06/07/2024', '07/07/2024', '22/06/2024', '23/06/2024', '05/07/2024', '07/07/2024', '19/07/2024', '03/07/2024', '06/07/2024', '08/07/2024', '12/07/2024', '19/07/2024', '21/07/2024', '13/07/2024', '22/07/2024' ],
    'TEAM': ['Brazil', 'Cameroon', 'Brazil', 'Latvia', 'Japan', 'Australia', 'Japan', 'Japan', 'Germany', 'France', 'Germany', 'France', 'France', 'France', 'France', 'Germany', 'USA'],
    'T SCORE': [81, 77, 71, 69, 89, 95, 84, 88, 104, 96, 66, 65, 67, 73, 82, 95, 92],
    'OPPONENT': ['Montenegro', 'Brazil', 'Philippines', 'Brazil', 'Australia', 'Japan', 'South Korea', 'South Korea', 'Japan', 'Turkey', 'France', 'Germany', 'Serbia', 'Canada', 'Australia', 'Netherlands', 'Germany'],
    'O SCORE': [72, 74, 60, 94, 90, 95, 84, 80, 83, 46, 90, 70, 89, 85, 83, 50, 88],
    'TYPE': ['Qualifying', 'Qualifying', 'Qualifying', 'Qualifying', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation', 'Preparation'],
    'ID': ['BRA1', 'CAM1', 'BRA2', 'LAT1', 'JAP1', 'AUS1', 'JAP2', 'JAP3', 'GER1', 'FRA1', 'GER2', 'FRA2', 'FRA3', 'FRA4', 'FRA5', 'GER3', 'USA1']
}

games = pd.DataFrame(data)
games.to_csv('games.csv', index=False)
