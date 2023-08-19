import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from src.services import get_trends

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='trends-graph'),
])


@app.callback(
    Output('trends-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    trends = get_trends()

    # Criar o gráfico usando os dados dos trends

    figure = {...}  # Substitua isso pelo código real de criação do gráfico

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
