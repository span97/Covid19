import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt



import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output , State

import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure()


year2020_dataset = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"

df = pd.read_csv(year2020_dataset)

unique_countries = df['Country'].unique()

max_infections = []
for i in unique_countries:
    MIR = df[df.Country == i].Confirmed.diff().max()
    max_infections.append(MIR)


df_MIR = pd.DataFrame()
df_MIR["Country"] = unique_countries
df_MIR["Max Infection Rate"] = max_infections

fig = px.choropleth(df, locations="Country", locationmode="country names",
                    color='Confirmed', animation_frame="Date", color_continuous_scale=["white", "grey", "green"])

fig_1 = px.choropleth(df, locations="Country", locationmode="country names",
                      color='Deaths', animation_frame="Date", color_continuous_scale=["white", "grey", "black"])

fig_2 = px.bar(df_MIR, x="Country", y="Max Infection Rate", color="Country", log_y=True)


fig.update_layout(

    margin=dict(l=100, r=100, t=50, b=50),
    paper_bgcolor="white",
    font_color="Black"

)

fig_1.update_layout(

    margin=dict(l=100, r=100, t=50, b=50),
    paper_bgcolor="white",
    font_color="Black"

)

app = dash.Dash()
app.layout = html.Div(children=[
    html.Div([
        html.H2(children='CORONA PANDEMIC 2020 '),
        html.H3(children='Covid-19 Confirmed cases '),

        dcc.Graph(figure=fig),
    ]),

    html.Div([
        html.H3(children='Covid-19 Deaths'),

        dcc.Graph(figure=fig_1)
    ]),

    html.Div([
        html.H3(children='Country and the maximum infection rates '),

        dcc.Graph(figure=fig_2)
    ]),


])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter















