import csv
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go 
df = pd.read_csv("data.csv")

student = df.loc[df['student_id']=='TRL_987']
fig = go.Figure(go.Bar(
    x = student.groupby("level")["attempt"].mean(),
    y = ['Level - 1' , 'Level - 2' , 'Level - 3' , 'Level - 4'],
    orientation = 'h'
))

fig.show()