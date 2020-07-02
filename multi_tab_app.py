import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State

import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1('App Title'),

    html.Div("""
        App Desc
    """),

    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Execution Tab', value='tab-1'),
        dcc.Tab(label='Result Tab', value='tab-2'),
    ]),

    html.Div(id='tabs-example-content')
])

# execution tab layout
execution_tab_layout = html.Div([
    html.Div(
        id = 'execution_grid',
        children = [
            html.Div(id='container-button-basic',children='Input the file path'),
            html.Div(dcc.Input(id='input-on-submit', type='text')),
            html.Button('Submit', id='submit-val', n_clicks=0)
        ]
    )
])


# update execution tab
@app.callback(
    Output('container-button-basic', 'children'),
    [
        Input('submit-val', 'n_clicks')
    ],
    [
        State('input-on-submit', 'value')
    ]
)
def update_output(n_clicks, fpath):
    if fpath:
        try:
            df = pd.read_csv(fpath)
            return f'Loaded {fpath} successfully.'
        except FileNotFoundError:
            return f'FileNotFound. Please check the file path'
    else:
        return 'Enter the file path'

# general layout
@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return execution_tab_layout
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])



if __name__ == '__main__':
    app.run_server(debug=True)