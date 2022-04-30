# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data/clean_daily_sales_data.csv')

fig = px.line(df, x="date", y="sales", title='Sales of Pink Morsel During the years')

app.layout = html.Div(children=[
    html.H1(children='Visualise the Sales of Pink Morsel in Soul Foods\'s'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.H2(children='As we can see on the linear graph, the sales of Pink Morsel did increase after January 15th 2021')
])

if __name__ == '__main__':
    app.run_server(debug=True)