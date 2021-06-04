import pandas as pd
import plotly.express as px
df = pd.read_csv("covid.csv")
figure = px.scatter(df, x = "cases", y = "country")
figure.show()