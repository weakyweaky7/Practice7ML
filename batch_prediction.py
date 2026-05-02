import sqlite3
import pickle

def main():
    conn = sqlite3.connect('batch_prediction.db')
    cursor = conn.cursor()

    cursor.execute("SELECT feature_1, feature_2, feature_3 FROM input_data")
    rows = cursor.fetchall()

    with open('trained_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    for row in rows:
        feature_1 = row[0]
        feature_2 = row[1]
        feature_3 = row[2]
        
        input_data = [[feature_1, feature_2, feature_3]]  
        prediction = model.predict(input_data)[0]  
    
        cursor.execute("INSERT INTO predictions (prediction) VALUES (?)", (prediction,))

    conn.commit()
    conn.close()
