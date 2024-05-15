import numpy as np
import pandas as pd
from datetime import datetime,timedelta
from sklearn.preprocessing import MinMaxScaler
import pickle


OD_2017_weather_agg = pd.read_csv('/Users/sayems_mac/BixiMatch/data/OD/OD_2017_weather_agg.csv')

# Load the model

loaded_model = pickle.load(open('/Users/sayems_mac/BixiMatch/model/linear_model.sav', 'rb'))

# Load the MinMaxScaler

minmaxx = pickle.load(open('/Users/sayems_mac/BixiMatch/model/minmaxx.pkl', 'rb'))  
minmaxy = pickle.load(open('/Users/sayems_mac/BixiMatch/model/minmaxy.pkl', 'rb'))



# Function to extract relevant historical data
def extract_historical_data(df, start_date, end_date):
    df['start_date'] = pd.to_datetime(df['start_date'])
    return df[(df['start_date'] >= start_date) & (df['start_date'] <= end_date)]



def predict_for_date(date):

    start_date = date - timedelta(days=530)
    end_date = date + timedelta(days=24)

    # #convert the date to the format in the data
    # start_date = start_date.strftime('%Y-%m-%d')
    # end_date = end_date.strftime('%Y-%m-%d')

    historical_data = extract_historical_data(OD_2017_weather_agg, start_date, end_date)

    # Prepare features for model (similar to your training setup)
    X_test = []
    for k in range(720, historical_data.shape[0] - 24):
        X_test.append(np.hstack((
            historical_data['num_trips'].values[k-720:k-1],           # last month usage
            historical_data['Description'].values[k-24:k+24],    
            historical_data['Temperature'].values[k-24:k+24],   
            historical_data['Wind_speed'].values[k-24:k+24],
            historical_data['num_week'].values[k],              
            historical_data['weekday'].values[k],                 
            historical_data['hour'].values[k],               
            1                     
        )).tolist())  

    X_test = np.array(X_test)

    # Normalize features
    X_test_norm = minmaxx.transform(X_test)

    # Predict

    y_pred_norm = loaded_model.predict(X_test_norm)

    # Denormalize prediction

    y_pred = minmaxy.inverse_transform(y_pred_norm)

    # return prediction of just 24 hours

    return y_pred[0:24]


if __name__ == '__main__':

    date = datetime(2017, 6,14)
    predictions = predict_for_date(date)
    print(predictions)


