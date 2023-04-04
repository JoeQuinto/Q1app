from dash import Dash, html
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__)


layout = html.Div([    
    dbc.Card([
        html.H3('Select a Dashboard',style={"margin-left":"0.3rem"} ),
        dbc.RadioItems(["Energy", "Employee Performance", "Sales"])
        ], style={"width":"20%", "background-color":"rgb(255,255,255,0.2)", 
                   "border": "1px rgb(200,100,200,0.5)","border-radius": "20px"}, 
        class_name="card border-primary mb-3 "),

    dbc.Card([
        html.H1("Dashboard", style={"margin":"auto"})
        ], style={"width":"80%", "background-color":"rgb(255,255,255,0.2)", 
                  "border": "1px rgb(200,100,200,0.5)", "border-radius": "25px"}, 
        class_name="card border-primary mb-3", )  
     
], style={"display":"flex"})




