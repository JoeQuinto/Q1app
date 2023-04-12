from dash import Dash, html, callback, Input, Output, State, dcc
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from plotly.graph_objects import *


dash.register_page(__name__)


layout = html.Div([    
    dbc.Card([
        html.H3('Select a Dashboard',style={"margin-left":"0.3rem"} ),
        dbc.RadioItems(["Energy", "Employee Performance", "Sales"], id='dashboard-select')
        ], style={"width":"20%", "background-color":"rgb(255,255,255,0.2)", 
                   "border": "1px rgb(200,100,200,0.5)","border-radius": "20px"}, 
        ),

    dbc.Card([
        
        html.Div(id= "dashb-content", style={'width':'100%'})
        ], 
        style={"width":"80%", "background-color":"rgb(255,255,255,0.2)", 
                  "border": "1px rgb(200,100,200,0.5)", "border-radius": "25px"}, 
        class_name="card border-primary mb-3", )  
     
], style={"display":"flex"})

#Energy Container -------------------------------------------------------------------

df = pd.read_csv('data/electric_nuclear.csv')
energy_g1 = px.line(df, x='Date', y='Consumed')
energy_g1.update_layout(margin={'l':2, 'r':2}, 
                        plot_bgcolor='rgba(0,0,0,0.1)', 
                        paper_bgcolor='rgba(255,255,255,0)')
energy_g2 = px.line(df, x='Date', y='Generated')
energy_g2.update_layout(margin={'l':2, 'r':2},
                        plot_bgcolor='rgba(0,0,0,0.1)', 
                        paper_bgcolor='rgba(255,255,255,0)')
ratio_tab = df.groupby(by='Year').apply(lambda x: x.loc[x['Consume_ratio'].idxmax(), 
                                                        ['Generated', 'Consumed', 'Month', 'Consume_ratio']])
ratio_tab['Consume_ratio'] = ratio_tab.Consume_ratio.round(decimals=2)

ratio_g = px.line(data_frame= ratio_tab.reset_index().sort_values(by='Year'),
                  x='Year', y='Consume_ratio')
ratio_g.update_layout(margin={'l':20, 'r':2},
                        plot_bgcolor='rgba(0,0,0,0.1)', 
                        paper_bgcolor='rgba(255,255,255,0)')

energy_container = html.Div([
    html.H3('Energy Consumption and Generation in USA 1973-2019', style={'margin-left':'0.5rem'}),
    html.Div([
        dcc.Graph(id="energy-g1", 
                figure= energy_g1, style={'width':'49%'}),
        dcc.Graph(id="energy-g1", 
                figure= energy_g2,style={'width':'49%'})], 
                style={'display':'flex', 'width':'100%', 'height': '20rem'}
    ),
    html.Div([
        html.H3('Top Generation-Consumption ratio by year', style={'font-size':'1rem', 'margin-left':'2rem'}),
        html.Div([    
            dash.dash_table.DataTable(ratio_tab.reset_index().sort_values(by='Consume_ratio',
                ascending=False).to_dict('records'),
                page_action='none',
                style_table={ 'overflowY': 'auto', 'height': '80%', 
                            'backgroundColor':'rgba(255,0,255,0.2)',
                            'margin-left':'2rem'}
                                        ),
            dcc.Graph(id='ratio-g', figure=ratio_g, style={'width':'65%', 'margin-left':'3rem'})
                
                ], style={'display':'flex', 'width':'100%', 'height':'20rem'})
    ])
         
    ])
    

#Sales Container -------------------------------------------------------------------


sales_container = html.Div([
    
    html.H3('Sales Content') ])  
    
#Employee Container -------------------------------------------------------------------

employee_container = html.Div([        
    
    html.H3('Employee Content') ])  


#Calbacks ------------------------------------------------------------------------------

@callback(
    Output('dashb-content', 'children'),
    Input('dashboard-select', 'value')
)
def dashboard_selector(dashboard):
    if dashboard == 'Energy':
        res = energy_container    
    elif dashboard == 'Sales':
        res = sales_container 
    elif dashboard == 'Employee Performance':
        res = employee_container 
    else:
        res = html.Div([html.H1("Dashboard", style={"margin":"auto"}),html.H3('No data selected yet') ])   
    
    return res


    



