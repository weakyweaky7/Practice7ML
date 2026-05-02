import sqlite3
import numpy as np

conn = sqlite3.connect('batch_prediction.db')
cursor = conn.cursor()

cursor.execute("SELECT feature_1, feature_2, feature_3 FROM input_data")
rows = cursor.fetchall()

X = np.array([row[:3] for row in rows]) 

print(f"X shape: {X.shape}")

y = np.array([350000.0, 400000.0, 250000.0, 380000.0, 410000.0, 260000.0, 450000.0, 470000.0, 320000.0, 330000.0, 340000.0, 360000.0, 380000.0, 390000.0, 400000.0, 420000.0, 430000.0, 440000.0])

print(f"X shape: {X.shape}, y shape: {y.shape}")

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X, y)

import pickle
with open('trained_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

conn.close()

