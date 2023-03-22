from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

app = Dash(__name__, use_pages=True,
	   meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}],
	    external_stylesheets=[dbc.themes.SOLAR]
	)



header = html.Div([
	
    html.Div([
        html.Img(src='assets/solo-logo2.png', style={'height' : '80px'},
		  className='spinning-logo'),
        html.Img(src='assets/solo-name2.png', style={'height' : '100px', 'padding-left':'20px'}, )], 
	    style={'padding-top':'10px'})
		 ,
		 
	html.H2('Insight View',	 
	    style={'font-size': '25px', 'color':'rgb(64, 130, 126)'}),
	
	], id='header')
    
	

sidebar_header = dbc.Row(
    [
        dbc.Col(html.H3("Q1App", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

	

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            
            html.Hr(),),


        dbc.Nav([    
                
            dbc.NavItem(
                dcc.Link(
                    f"{page['name']} ", href=page["relative_path"]
                        )
                    )
                        for page in dash.page_registry.values()   

            
        ], vertical=True, pills = True, )], id='sidebar') 





content= html.Div(dash.page_container, id='page-content', style={ 'lenght':'100%', 'bottom' :'0'})


app.layout=html.Div(html.Div([sidebar, 
			      html.Div([header, content], style={'width':'100%'})], 
		  style={'display':'flex'}), id='page')

if __name__ == '__main__':
	app.run_server(debug=True)