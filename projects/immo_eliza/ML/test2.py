import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import OneHotEncoder
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import optuna 

df = pd.read_csv("clean_datasett.csv")

y = df['Price']
X = df.drop(['Price'], axis=1)
"""
def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 2000),
        "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.1, log=True),
        "depth": trial.suggest_int("depth", 1, 10),
        "subsample": trial.suggest_float("subsample", 0.05, 1.0),
        "colsample_bylevel": trial.suggest_float("colsample_bylevel", 0.05, 1.0),
        "min_data_in_leaf": trial.suggest_int("min_data_in_leaf", 1, 100),
    }

    model = CatBoostRegressor(**params, silent=True)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    print(f'RMSE score: {rmse}')
    r2 = r2_score(y_test, predictions)
    print(f'R² score: {r2}')
    print(model.score(X_test, y_test))

    y_pred = model.predict(X_test)

    print(mean_absolute_error(y_test, y_pred))
    return rmse
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=100)

print('Best hyperparameters:', study.best_params)
print('Best RMSE:', study.best_value)


"""
random_states = np.arange(start=29, stop=30)
params = {'n_estimators': 1952, 
          'learning_rate': 0.09958080678882802, 
          'depth': 10, 
          'subsample': 0.9024150233634263, 
          'colsample_bylevel': 0.26048065199333004, 
          'min_data_in_leaf': 24
    }
r2 = []
mae=[]
for i in tqdm(random_states):
    X_train, X_test, y_train,y_test = train_test_split(X, y,test_size=0.20, random_state=i)
    model = CatBoostRegressor(**params,loss_function='RMSE',verbose=100)
    model.fit(X_train, y_train, verbose=100)
    prediction =model.predict(X_test)
    mean =mean_absolute_error(y_test,prediction) 
    mae.append(mean)
    score = r2_score(y_test, prediction)
    r2.append(score)
    rmse = mean_squared_error(y_test, prediction, squared=False)
    print(f'RMSE score: {rmse}')
    print(model.score(X_test, y_test))
print(r2)
print(mae)
