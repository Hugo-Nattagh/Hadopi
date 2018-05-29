import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# import csv file
df = pd.read_csv("hadopi_chiffres_bruts2.csv")

# convert object to datetime
df['annee_mois'] = df['annee_mois'].str.replace('-', ' ')
df['annee_mois'] = pd.to_datetime(df['annee_mois'])

# get the grey background for the plots
plt.style.use('seaborn-darkgrid')

# first plot
cols = ['Premier_Avertissement', 'Deuxieme_Avertissement', 'Transmission_Parquet']
# df.plot(x='annee_mois', y=cols, color=('#1F77B4', '#FF7F0E', '#B40404'))

# second plot
df.plot(x='annee_mois', y='Transmission_Parquet', color='#B40404', label='Transmission au Parquet')

# to rotate x values (I didn't use it in the end)
# plt.xticks(rotation=90)

# create dataframe with yearly budget
d = {'Année': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017], 'Budget': [10, 11.4, 11, 8.4, 5.6, 5.52, 7.8, 9]}
df_bud = pd.DataFrame(data=d)

# third plot
# df_bud.plot(x='Année', y='Budget', ylim=(0, 13), color='green', label='Budget en millions')

# remove x axis title
plt.xlabel("")

# move legends
plt.legend(loc='upper left')

# move legends and give labels
# plt.legend(loc='upper left', labels=['Premier Avertissement', 'Deuxième Avertissement', 'Transmission au Parquet'])

# show plot
plt.show()
