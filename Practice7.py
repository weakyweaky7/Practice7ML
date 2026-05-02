import sqlite3
import pickle

conn = sqlite3.connect('batch_prediction.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS input_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_1 REAL,
    feature_2 INTEGER,
    feature_3 INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prediction REAL,
    prediction_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
''')

cursor.execute('''
INSERT INTO input_data (feature_1, feature_2, feature_3) 
VALUES (1500, 3, 2);
''')
cursor.execute('''
INSERT INTO input_data (feature_1, feature_2, feature_3) 
VALUES (2000, 4, 3);
''')
cursor.execute('''
INSERT INTO input_data (feature_1, feature_2, feature_3) 
VALUES (1200, 2, 1);
''')

cursor.execute('''
INSERT INTO predictions (prediction) 
VALUES (350000.0);
''')
cursor.execute('''
INSERT INTO predictions (prediction) 
VALUES (400000.0);
''')
cursor.execute('''
INSERT INTO predictions (prediction) 
VALUES (250000.0);
''')

for i in range(9, 15): 
    cursor.execute("INSERT INTO predictions (prediction) VALUES (?)", (350000.0 + i * 10000,))

conn.commit()
conn.close()
