import dash 
from dash import Dash, html, DiskcacheManager
import dash_gif_component as gif

dash.register_page(__name__, path='/')

layout = html.Div([   

      html.H1('Home')
         
    
    
])

#gif.GifPlayer(
 #       gif='../assets/QData.gif',
 #       still='../assets/QData.gif',
 #       autoplay=True
 #       )