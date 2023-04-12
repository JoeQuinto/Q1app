from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

app = Dash(__name__, use_pages=True,
	   meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}],
	    external_stylesheets=[dbc.themes.YETI], suppress_callback_exceptions=True
	)

header = html.Div([
	
    html.Div([
        html.Img(src='assets/solo-logo2.png', style={'height' : '2.5rem', "padding-top": "0.2rem"},
		  className='spinning-logo'),
        html.Img(src='assets/solo-name2.png', style={ 'padding-left':'0.7rem', 'margin-top': '2rem !important'},
		 className='logo-name' )], 
	    )
		 ,
		 
	html.H2('Insight View',	 
	    style={'font-size': '0.8rem', 'color':'rgb(64, 130, 126)', 'padding-left' : '4rem'}),
	
	], id='header')   

	

navbar = dbc.Navbar(
				dbc.Nav(
					[
						dbc.Col(
							dbc.NavItem(header, style={ 'display':'flex', "margin":"auto"}),
							width={"width":"33%", "order": "2"},
							style={ 'display':'flex', "margin":"auto"},
						),
						dbc.Col(
							[
								dbc.NavLink("Home", href="/", active="exact"),
								dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
								dbc.NavLink("About", href="/about", active="exact"),
							],
							width={"size": "auto", "order": "1"},
							style={"width":"33%", "display":"flex"},
						),
						dbc.Col(
							html.Br(),
							style={"width":"33%", "order":"3"}
						)
					], 
					
					style={"display": "flex", "width":"100%", "height":"3.1rem" }					
				),

				id="navbar",
				className="navbar navbar-expand-lg navbar-dark bg-dark",
				style={"display": "flex", "flex-direction": "row" }
			)

content= html.Div(dash.page_container, id='content')


app.layout=html.Div([navbar, content], id='page')

if __name__ == '__main__':
	app.run_server(debug=True)