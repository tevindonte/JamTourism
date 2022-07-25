from operator import index
from unicodedata import name
import matplotlib.pyplot as plt
import plotly.express as px
from geopandas import gpd
from shapely import wkt
import pandas as pd
import numpy as np
import fiona
import csv

#Matplot Pie Chart Method 1 - Visitors Reasons
df = pd.read_csv ('travel.csv')
font1 = {'family':'Fantasy','color':'black','size':20}
sums = df.groupby(df["Reason"])["Visitor"].sum()
explode = (.05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05)
plt.title('TRAVEL REASONS', fontdict = font1);
plt.axis('equal');
plt.pie(sums, explode=explode);
plt.labels=(sums.index);
plt.legend(labels=sums.index,
          title="Reasons",
          loc="center left",
          bbox_to_anchor=(.9, 0, 0.5, 1))
plt.show()



#Plotly Pie Chart Method 2 - Visitors Reasons
df = pd.read_csv ('travel.csv')
fig = px.pie(df, values='Visitor', names='Reason', title='TRAVEL REASONS')
fig.show()



#Matplot Bar Graph Method- Visitors Reasons
data = pd.read_csv('travel.csv')
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 2])
plt.bar(X, Y, color='g')
plt.title('TRAVEL REASONS', fontdict = font1);
plt.xlabel("Reasons")
plt.ylabel("Number of Visitors")
plt.show()



#Plotly Stacked Graph
df = pd.read_csv ('Port Reasons.csv')
fig = px.bar(df, y='Visitor', x='Port', title='Tourists Airport Entry and Reason', hover_data=['Reason'], barmode = 'stack', text='Reason')
fig.show()



#Pie Chart For Airports
df = pd.read_csv ('Port Reasons.csv')
fig = px.pie(df, values='Visitor', names='Port', title='Entry')
fig.show()



df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title('Number of Visitors Per Country', fontdict = font1);
plt.xlabel("Countries")
plt.ylabel("Number of Visitors")
plt.show()



#Horizontal Bar Chart for Countries Visitor Count
df = pd.read_csv ('visitorscountry.csv')
fig = px.bar(df, x="visitors", y="country", orientation='h')
fig.show()



#World Data Distribution
df = pd.read_csv('visitorscountry.csv')
fig = px.choropleth(df, locations="CODE",
                    color="visitors",
                    hover_name="country",
                    title = "Visitors plotted by Country", color_continuous_scale=px.colors.diverging.BrBG, color_continuous_midpoint=0,)
fig.show()

