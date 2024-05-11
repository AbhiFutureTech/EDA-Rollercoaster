import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sns

df= pd.read_csv(r"E:\projects\Chat Bot\coaster_db.csv")

print(df.shape)
print(df.head(5))
print(df.columns)
print(df.dtypes)
print(df.describe())

# Example of dropping columns
# df.drop(['Opening date'], axis=1)

df = df[['coaster_name',
    # 'Length', 'Speed',
    'Location', 'Status',
    # 'Opening date',
    #   'Type',
    'Manufacturer',
#Height restriction', 'Model', 'Height'
#        'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
#        'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
#        'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
#        'Track layout', 'Fastrack available', 'Soft opening date.1',
#        'Closing date',
#     'Opened',
    # 'Replaced by', 'Website',
#        'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
#        'Single rider line available', 'Restraint Style',
#        'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced',
        'latitude', 'longitude',
    'Type_Main',
       'opening_date_clean',
    #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph',
    #'height_value', 'height_unit',
    'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()

df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

# Rename our columns
df = df.rename(columns={'coaster_name':'Coaster_Name',
                   'year_introduced':'Year_Introduced',
                   'opening_date_clean':'Opening_Date',
                   'speed_mph':'Speed_mph',
                   'height_ft':'Height_ft',
                   'Inversions_clean':'Inversions',
                   'Gforce_clean':'Gforce'})

print(df.isna().sum())
print(df.loc[df.duplicated()])


# Check for duplicate coaster name
print(df.loc[df.duplicated(subset=['Coaster_Name'])].head(5))

# Checking an example duplicate
print(df.query('Coaster_Name == "Crystal Beach Cyclone"'))

print(df.columns)

df = df.loc[~df.duplicated(subset=['Coaster_Name','Location','Opening_Date'])] \
    .reset_index(drop=True).copy()

print(df['Year_Introduced'].value_counts())

ax = df['Year_Introduced'].value_counts() \
    .head(10) \
    .plot(kind='bar', title='Top 10 Years Coasters Introduced')
print(ax.set_xlabel('Year Introduced'))
print(ax.set_ylabel('Count'))

ax: object = df['Speed_mph'].plot(kind='hist',
                          bins=20,
                          title='Coaster Speed (mph)')
print(ax.set_xlabel('Speed (mph)'))

print(df['Type_Main'].value_counts())


df.plot(kind='scatter',
        x='Speed_mph',
        y='Height_ft',
        title='Coaster Speed vs. Height')
print(plt.show())

ax = df.query('Location != "Other"') \
    .groupby('Location')['Speed_mph'] \
    .agg(['mean','count']) \
    .query('count >= 10') \
    .sort_values('mean')['mean'] \
    .plot(kind='barh', figsize=(12, 5), title='Average Coast Speed by Location')
ax.set_xlabel('Average Coaster Speed')
print(plt.show())

