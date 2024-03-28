import pandas as pd
from joblib import dump
from sklearn.calibration import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv('meteor.csv')

le = LabelEncoder()
df = df.drop(['name', 'id', 'nametype', 'fall', 'GeoLocation'], axis = 1)

for x in df.index:
  if df.loc[x, 'mass'] > 16000:
    df.drop(x, inplace = True)
  elif df.loc[x, 'mass'] < 0:
    df.drop(x, inplace = True)

df['recclass'] = le.fit_transform(df['recclass'])

df = df.dropna()

Y = df['mass']

X = df.drop(['mass'], axis = 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.05, random_state = 42)


model = RandomForestRegressor(max_depth = 10, min_samples_split = 4, n_estimators = 300)

model.fit(X_train, Y_train)

Y_real = Y_train
Y_pred = model.predict(X_train)
train_error = mean_absolute_error(Y_real, Y_pred)

Y_real = Y_test
Y_pred = model.predict(X_test)
test_error = mean_absolute_error(Y_real, Y_pred)

print("r2 score: ", r2_score(Y, model.predict(X)))
print("Erro de treino: ", train_error, "/ Erro de teste: ", test_error)
dump(model, "randomForestMass.pkl")
dump(le, "label_encoder.pkl")