# Import your libraries
import pandas as pd
import datetime as dt
import numpy as np

#Sort by id and time, then create a date column
df1 = facebook_web_log.sort_values(['user_id', 'timestamp'])
df1['date'] = df1['timestamp'].dt.date
df1
#group by id and date, then filter out the latest page_load
df2 = df1.groupby(['user_id', 'date', 'action'])['timestamp'].last().reset_index().query('action == "page_load"')

#group by id and date, then filter out the first page_load
df3 = df1.groupby(['user_id', 'date', 'action'])['timestamp'].first().reset_index().query('action == "page_exit"')

#join df2 and df3, then calculate time diff within the sameday
df4 = pd.merge(df2, df3, how = 'outer', on =['user_id', 'date'])
df4['diff'] = df4['timestamp_y'] - df4['timestamp_x']
df4

# groupby user_id and calculate the avg session time
df4.dropna().groupby('user_id')['diff'].apply(np.mean).reset_index()
