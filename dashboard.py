import dash
from dash import dcc, html
import dash_table
import pandas as pd

# Carregar dados do Excel
df = pd.read_excel('dados.xlsx')

# Inicializar o app do Dash
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Dashboard de Testes'),

    html.Div(children='''
        Dados extraídos do arquivo XML e apresentados em um dashboard.
    '''),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={
            'height': 'auto',
            'minWidth': '0px', 'maxWidth': '180px',
            'whiteSpace': 'normal'
        },
        page_size=10
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['TestId'], 'y': df['Output'], 'type': 'bar', 'name': 'Output'},
            ],
            'layout': {
                'title': 'Saída dos Testes'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
