import dash
import dash_html_components as html
import dash_core_components as dcc
import datetime as dt
from dash.dependencies import Input, Output

import dash_table


###################
import dash_bootstrap_components as dbc
import pandas as pd
data = [['US', 10], ['CA', 15], ['CA', 30], ['SAIR', 20], ['QIR', 25], ['MTL', 25]] 
df = pd.DataFrame(data, columns = ['Country', 'Age']) 
##############


#########################
colors = {
    'background': '#FFFFFF',
    'text': '#00AFE9'}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
logo_src = "https://1000logos.net/wp-content/uploads/2016/10/Barclays-Logo.png"
options = {'Country': ['India','USA','China'],'Region':['Americas','Europe & Middle East','Pacific'],'DM-EM Flag': ['DM','EM'],'ACWI':['ACWI']} 



############### form #################

# email_input = dbc.FormGroup(
#     [
#         dbc.Label("Email", html_for="example-email-row", width=2),
#         dbc.Col(
#             dbc.Input(
#                 type="email", id="example-email-row", placeholder="Enter email"
#             ),
#             width=10,
#         ),
#     ],
#     row=True,
# )

# password_input = dbc.FormGroup(
#     [
#         dbc.Label("Password", html_for="example-password-row", width=2),
#         dbc.Col(
#             dbc.Input(
#                 type="password",
#                 id="example-password-row",
#                 placeholder="Enter password",
#             ),
#             width=10,
#         ),
#     ],
#     row=True,
# )

# radios_input = dbc.FormGroup(
#     [
#         dbc.Label("Radios", html_for="example-radios-row", width=2),
#         dbc.Col(
#             dbc.RadioItems(
#                 id="example-radios-row",
#                 options=[
#                     {"label": "First radio", "value": 1},
#                     {"label": "Second radio", "value": 2},
#                     {
#                         "label": "Third disabled radio",
#                         "value": 3,
#                         "disabled": True,
#                     },
#                 ],
#             ),
#             width=10,
#         ),
#     ],
#     row=True,
# )

# form = dbc.Form([email_input, password_input, radios_input])

############################################

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[

    html.Img(
        src = logo_src,
        style={
            'height': '10%',
            'width': '10%',
            'float': 'right',
            'position': 'relative',
        }
        ),
    html.Div([
        html.H1(children='MSCI Rebalance'), 
        html.H5(children='Carry out a rebalance for any country/region/DM-EM Market/ACWI')
        ], style={'margin-top':20,'textAlign': 'center','position': 'relative', 'color': colors['text']}),
    
    html.Hr(),
    html.Div(
        [html.Div(
            [html.Label(children = 'Select country',style = {'color': colors['text']} ),
            dcc.Dropdown(id = 'countries-dropdown',
                placeholder="Type something...",
                options=[{'label':'United','value':'US'},{'label':'Canada','value':'CA'}],
                value='MTL'
            )],className = "six columns", style={'float': 'left','position': 'relative','margin-left':20}),
        html.Div(
            [html.Label(children = 'Date of Used data',style = {'color': colors['text']} ),
            dcc.DatePickerSingle(
                id='date-picker-single',
                date= dt.date(2020,5,24)
            )], 
            className = "four columns", style={'float': 'right','textAlign': 'center','position': 'relative'}),
        ], className = "row", style = {'margin': 3}),
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
                # labelStyle={'display': 'inline-block'},
                value=['SAIR','QIR']
            )] ,className = "six columns", style={'float': 'left','position': 'relative','margin-left':20}),
        
        # html.Hr(),
        html.Div(
            [html.Div('Click below to generate the results',style = {'color': colors['text']}),
            html.Button('Submit', id='button', style = {'textAlign': 'center','color': colors['text']},
            )],className = "four columns", style={'float': 'right','textAlign': 'center','position': 'relative'})
        ], className = "row", style = {'margin': 3}),

    html.Br(),

    dash_table.DataTable(id='table'),
    
    # html.Div([form])
    # html.P(id = 'date_out')

    
], className = "ten columns offset-by-one")




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