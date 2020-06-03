import dash
import dash_html_components as html
import dash_core_components as dcc
import datetime as dt
from dash.dependencies import Input, Output

import dash_table

import config


###################
import dash_bootstrap_components as dbc
import pandas as pd
data = [['US', 10], ['CA', 15], ['CA', 30], ['SAIR', 20], ['QIR', 25], ['MTL', 25]] 
df = pd.DataFrame(data, columns = ['Country', 'Age']) 
##############


#########################
colors = {
    # 'background': '#FFFFFF',
    'text': '#00AFE9'}

BS = "https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
# available_themes =  ['CERULEAN', 'COSMO', 'CYBORG', 'DARKLY', 'FLATLY', 'JOURNAL', 'LITERA', 'LUMEN', 'LUX', 'MATERIA', 'MINTY', 'PULSE', 'SANDSTONE', 'SIMPLEX', 'SKETCHY', 'SLATE', 'SOLAR', 'SPACELAB', 'SUPERHERO', 'UNITED', 'YETI']
stylesheets = [dbc.themes.FLATLY]
logo_src = config.logo_src
options = {'Country': ['India','USA','China'],'Region':['Americas','Europe & Middle East','Pacific'],'DM-EM Flag': ['DM','EM'],'ACWI':['ACWI']} 


######################


app = dash.Dash(__name__, external_stylesheets = stylesheets)
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# style={'backgroundColor': colors['background']},

app.layout = html.Div( children=[

    html.Div([
        html.Img(
        src = logo_src,
        style={
            'height': '10%',
            'width': '10%',
            'float': 'right',
            'position': 'relative',
        }
        ), 

        ]),
    html.Div([
        html.H1(children='MSCI Rebalance'), 
        html.H5(children='Carry out a rebalance for any country/region/DM-EM Market/ACWI')
        ], style={'margin-top':20,'textAlign': 'center','position': 'relative', 'color': colors['text']},className="m-5"),
    
    html.Hr(),
    html.Div(
        [
        html.Div(
            [html.Div([html.Label(children = 'Date of Used data',style = {'color': colors['text'],'margin-left':20} ),], className="row"),
            html.Div([dcc.DatePickerSingle(
                id='date-picker-single',
                date= dt.date(2020,5,24),
                style = {'margin-left':20}
            )], className="row")
                
                
            ], 
            className = "col", style={'float': 'left','textAlign': 'left','position': 'relative'}),
        html.Div(
            [html.Label(children = 'Select country',style = {'color': colors['text']} ),
            dcc.Dropdown(id = 'countries-dropdown',
                placeholder="Type something...",
                options=[{'label':'United','value':'US'},{'label':'Canada','value':'CA'}],
                value='MTL'
            )],className = "col-8", style={'float': 'right','position': 'relative','margin-left':20})
        ], className = "row", style = {'margin-top': 1}),

    ######################################################################### 

    html.Br(),
    html.Div([
        html.Div(
            [html.Label(children = 'Rebalance Type',style = {'color': colors['text']}),
            dcc.RadioItems(
                id = 'radio',
                options=[
                    {'label': 'Semi Annual Review (May & Nov)', 'value': 'SAIR'},
                    {'label': 'Quarter Review (Feb & Aug)', 'value': 'QIR'}
                ],
                labelStyle={'display': 'inline-block', 'margin-right':50},
                value=['SAIR','QIR']
            )] , style={'float': 'left','position': 'relative','margin-left':20}),
        
        ], className = "row", style = {'margin-bottom': 1}),
        


    #########################################
    html.Hr(),
    html.Div([
       
        # html.Hr(),
        html.Div(
            [html.Div('Click below to generate the results',style = {'color': colors['text']}),
            html.Button('Submit', id='button', style = {'textAlign': 'center','color': colors['text'],'margin-top':15},
            )], style={'textAlign': 'center','position': 'relative'})
        ], className = "row justify-content-center" , style={'float': 'center','position': 'relative', 'color': colors['text']}),

    html.Br(),
    html.Div([
        html.Div([
            dash_table.DataTable(id='table'),
        ], className="col-6")
        
        ],className = "row justify-content-center" , style={'position': 'relative'}),
    
    
    # html.Div([form])
    # html.P(id = 'date_out')

    
], className = "m-5")




# app.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })





@app.callback([Output("table", "data"), Output('table', 'columns')],
    [Input('countries-dropdown', 'value'), Input('radio', 'value')])

def update_table(selected_cont, radio):
    if radio == 'SAIR':    
        temp = df[df['Country'] == selected_cont]
    else:
        temp = df
    column = [{"name": i, "id": i} for i in temp.columns]
    return temp.to_dict('records'), column



@app.callback(Output("date_out", "children"),
    [Input('date-picker-single', 'date')])
def update_table(dat):
    return dat


if __name__ == '__main__':
    app.server.run(debug = True)