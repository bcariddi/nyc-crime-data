import pandas as pd

#data = pd.read_csv('NYPD_Complaint_Data_Historic.csv', low_memory=False)
#data['CMPLNT_FR_DT'] = pd.to_datetime(data['CMPLNT_FR_DT'], errors='coerce')
#df = data[(data['CMPLNT_FR_DT'] > '2015-01-01')]
#df.to_csv('Filtered_NYPD_Data.csv', encoding='utf-8', index=False)

data = pd.read_csv('Filtered_NYPD_Data.csv', low_memory=False)
data['CMPLNT_FR_DT'] = pd.to_datetime(data['CMPLNT_FR_DT'], errors='coerce')
df = data[(data['CMPLNT_FR_DT'] > '2017-12-31')]
df = df[(df['CMPLNT_FR_DT'] < '2019-01-01')]
df.to_csv('2018_NYPD_Data.csv', encoding='utf-8', index=False)
