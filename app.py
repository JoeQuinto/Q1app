from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

app = Dash(__name__, use_pages=True,
	   meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}],
	    external_stylesheets=[dbc.themes.YETI]
	)



header = html.Div([
	
    html.Div([
        html.Img(src='assets/solo-logo2.png', style={'height' : '30px'},
		  className='spinning-logo'),
        html.Img(src='assets/solo-name2.png', style={'height' : '30px', 'padding-left':'20px'}, )], 
	    style={'padding-top':'2px'})
		 ,
		 
	html.H2('Insight View',	 
	    style={'font-size': '15px', 'color':'rgb(64, 130, 126)', 'padding-left' : '50px'}),
	
	], id='header')   

	

sidebar1 = dbc.Navbar(
	dbc.Nav(
	[
	dbc.NavLink('Home', href="/", active='exact'),
	dbc.NavLink('Dashboard', href="/dashboard", active='exact'),
	dbc.NavItem(header)
    ]
    ), id='sidebar1', class_name="navbar navbar-expand-lg navbar-dark bg-dark"
)





content= html.Div(dash.page_container, id='page-content', style={ 'lenght':'100%', 'bottom' :'0'})


app.layout=html.Div([sidebar1, content, ], 
		  style={'display':'100%'}, id='page')

if __name__ == '__main__':
	app.run_server(debug=True)