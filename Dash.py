import dash
import dash_html_components as html
import dash_core_components as dcc
import datetime as dt
from dash.dependencies import Input, Output

import dash_table

colors = {
    'background': '#FFFFFF',
    'text': '#00AFE9'}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

options = {'Country': ['India','USA','China'],'Region':['Americas','Europe & Middle East','Pacific'],'DM-EM Flag': ['DM','EM'],'ACWI':['ACWI']} 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        
    html.H1(
        children='MSCI Rebalance',
        style={
            'textAlign': 'center',
            'color': colors['text']
        })
    , 
    
html.H5(children='Carry out a rebalance for any country/region/DM-EM Market/ACWI', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Label(children = 'Date of Used data',style = {'color': colors['text']} ),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date= dt.date(2020,5,24)
    ),
    
###############################################################################    
    html.Label(children = 'Select',style = {'color': colors['text']} ),
    dcc.Dropdown(id = 'countries-radio',
        options=[{'label':'United','value':'US'},{'label':'Canada','value':'CA'}],
        value='MTL'
    ),
 ######################################################################### 
    
    html.Label(children = 'Rebalance Type',style = {'color': colors['text']}),
    dcc.RadioItems(
        options=[
            {'label': 'Semi Annual Review (May & Nov)', 'value': 'SAIR'},
            {'label': 'Quarter Review (Feb & Aug)', 'value': 'QIR'}
        ],
        labelStyle={'display': 'inline-block'},
        value=['SAIR','QIR']
    ),
    html.Hr(),
    html.Div('Click below to generate the results'),
    html.Button('Submit', id='button',style = {'textAlign': 'center','color': colors['text']},
    ),
    dash_table.DataTable(
    id='table')
    
])   
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})
@app.callback([Output("table", "data"), Output('table', 'columns')],
    [Input('countries-radio', 'value')])

def update_table(selected_cont):
    temp = df[df['Country'] == selected_cont]
    column = [{"name": i, "id": i} for i in temp.columns]
    return temp.to_dict('records'), column

if __name__ == '__main__':
    app.server.run()