from dash import html
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/about")

layout = dbc.Card([
    html.H1("About", style={"margin":"auto", "padding":"0.5rem"}),
    html.P("Sit id minim minim veniam. Adipisicing minim in adipisicing nostrud incididunt. Esse adipisicing exercitation dolor laboris eu exercitation magna irure tempor. Anim laborum eiusmod dolor dolor officia laboris qui nulla nulla. Exercitation dolore nostrud sunt laboris ut sint cillum incididunt. Ex velit non sunt cillum. Incididunt in velit eu do cillum duis labore adipisicing ipsum nostrud id culpa cupidatat sint. Eiusmod amet mollit in sunt est officia eu tempor deserunt in ex eiusmod. Irure occaecat eu et exercitation non eiusmod in eu eu deserunt sit. Sint labore esse consequat labore non veniam nisi mollit.",
           style={"padding":"0.8rem"})
    ], style={"background-color":"rgb(255,255,255,0.2)",
                                                      "border":"1px", "border-radius":"20px"},
    class_name="card border-primary mb-3"
)