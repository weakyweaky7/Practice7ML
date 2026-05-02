import pandas as pd
import sqlite3

conn = sqlite3.connect('batch_prediction.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM predictions")
predictions = cursor.fetchall()

df = pd.DataFrame(predictions, columns=['ID', 'Prediction', 'Timestamp'])
print(df)

conn.close()