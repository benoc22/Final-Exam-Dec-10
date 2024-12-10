import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv")#importing file

#Rideship over time (1)
st.write("Total Ridership Over Time")
plt.figure(figsize=(12,8))
plt.plot(df['datetime'], df['cnt'], label='Total Ridership', color='blue')
plt.xlabel('Date')
plt.ylabel('Total Ridership')
plt.title('Total Ridership Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot()

#Plot total rideship by season (2)
st.write("Total Ridership by Season")
seasonal_counts = df.groupby('season')['cnt'].sum().sort_index()
seasonal_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
seasonal_counts.index = season_counts.index.map(season_labels)
plt.figure(figsize=(12,8))
sns.barplot(x=season_counts.index, y=season_counts.values, palette="viridis")
plt.xlabel('Season')
plt.ylabel('Total Ridership')
plt.title('Total Ridership by Season')
st.pyplot()

#Total rideship with rolling average (3)
st.write("Total Ridership with Rolling Average")
avg_type = st.radio("Select Rolling Average", options=["7-day Average", "14-day Average"])
if avg_type == "7-day Average": #Rolling avg
    rolling_window = 7
else:
    rolling_window = 14
df.set_index('datetime', inplace=True)
df['rolling_avg'] = df['cnt'].rolling(window=rolling_window).mean() #rolling avg for proper column
plt.figure(figsize=(10,6))
plt.plot(df.index, df['cnt'], label='Total Ridership', alpha=0.4)
plt.plot(df.index, df['rolling_avg'], label=f'{rolling_window}-Day Rolling Average', color='blue', linewidth=1)
plt.xlabel('Date')
plt.ylabel('Total Ridership')
plt.title(f'Total Ridership with {rolling_window}-Day Rolling Average')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot()

