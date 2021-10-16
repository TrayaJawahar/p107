import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')

means = df.groupby(["student_id" , "level"] , as_index=False)["attempt"].mean()

fig = px.scatter( means ,x="student_id" , y ="level" , color="attempt" , size ="attempt")

fig.show()
