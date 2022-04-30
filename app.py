# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data/clean_daily_sales_data.csv')

fig = px.line(df, x="date", y="sales", title='Sales of Pink Morsel During the years')

region = [
    {'label': 'North', 'value': 'north'},
    {'label': 'South', 'value': 'south'},
    {'label': 'East', 'value': 'east'},
    {'label': 'West', 'value': 'west'},
    {'label': 'All Regions', 'value': 'all'},
]

# Creating a function to avoid DRY while switching between regions in graph


def generate_figure(data):
    figure = px.line(data, x="date", y="sales", title="Pink Morsel Sales")
    return figure


app.layout = html.Div(children=[
    html.Div([
        html.Div([
            html.Div([
                html.H1(children='Visualise the Sales of Pink Morsel in Soul Foods\'s'),
            ]),
            html.H2('Select by Region:'),
            dcc.RadioItems(
                id="region-radio",
                options=region,
                value='all'
            ),
            html.Br(),
            dcc.Graph(
                    id='show_figure',
                    figure=generate_figure(df)
            ),
        ], style={
            'font-size': '20px',
            'backgroundColor': '#6098E6',
            'padding': '20px 20px',
            'color': '#0D3763',
            }),
        html.H2(
            children='As we can see on the linear graph, the sales of Pink Morsel did increase after January 15th 2021'
        )
    ], style={'fontFamily': 'monospace', 'textAlign': 'center'}),
])

# Using callback to update the current graph into the one needed by region


@app.callback(
    Output('show_figure', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        return generate_figure(df)
    return generate_figure(df[df['region'] == selected_region])


if __name__ == '__main__':
    app.run_server(debug=True)
