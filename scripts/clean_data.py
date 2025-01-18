# Script to ingest lifting data csv file, clean and restructure data

import pandas as pd
import datetime

def convert_to_minutes(duration):
    # function to convert workout duration field to just minutes
    hours = 0
    minutes = 0

    if 'h' in duration:
        parts = duration.split('h')
        hours = int(parts[0])
        if 'm' in parts:
            minutes = int(parts[1].strip.replace('m',''))
    elif 'm' in duration:
        minutes = int(duration.replace('m',''))
    
    return hours * 60 + minutes

raw_lifting_data_df = pd.read_csv(f'data_raw/strong_lifting_data_export_RAW.csv')       # read in lifting data csv

print(raw_lifting_data_df.head())

raw_lifting_data_df.drop(['Distance','Seconds','RPE','Notes','Workout Notes'])          # drop unused columns

raw_lifting_data_df['Date'] = pd.to_date(raw_lifting_data_df['Date'])                   # convert 'Date' column to datetime type

