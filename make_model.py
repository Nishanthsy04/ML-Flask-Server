import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("rainfall_data.csv")
data = data.fillna(0)
names = []
group = data.groupby('SUBDIVISION')[['YEAR','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']]

# Iterate over each unique subdivision
for subdivision, group_data in group:
    df = group_data.melt(['YEAR']).reset_index()
    df = df[['YEAR', 'variable', 'value']].reset_index().sort_values(by=['YEAR', 'index'])
    df.columns = ['Index', 'Year', 'Month', 'Avg_Rainfall']
    Month_map = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9,
                 'OCT': 10, 'NOV': 11, 'DEC': 12}
    df['Month'] = df['Month'].map(Month_map)
    df.drop(columns="Index", inplace=True)

    X = np.asanyarray(df[['Year', 'Month']]).astype('int')
    y = np.asanyarray(df['Avg_Rainfall']).astype('int')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

    random_forest_model = RandomForestRegressor(max_depth=100, max_features='sqrt', min_samples_leaf=4,
                                                min_samples_split=10, n_estimators=800)
    random_forest_model.fit(X_train, y_train)

    # Save the model using the subdivision name as the file name
    model_file_name = f"models/{subdivision}.pkl"
    names.append(subdivision)
    file = open(model_file_name, "wb")
    pickle.dump(random_forest_model, file)
    file.close()


print(names)