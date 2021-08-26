import pandas as pd
import plotly_express as px
df=pd.read_csv('C:/Users/Bajwa/Downloads/data2.csv')
fig = px.scatter(df, x="student_id", y="level", size="attempt", color="attempt")
fig.show()