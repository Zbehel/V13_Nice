from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.graph_objs as go


# Load data
df = pd.read_csv('https://raw.githubusercontent.com/zacbe/master/#v13.csv')
mapbox_access_token = ''

# Create app
app = Dash(__name__)

# Create layout
app.layout = html.Div([
    dcc.Graph(
        id='graph',
        figure=px.scatter_mapbox(
            df,
            lat='lat',
            lon='lng',
            zoom=1,
            height = 600,
            width = 800,
        ).update_layout(mapbox=dict(accesstoken = mapbox_access_token,
                                    center=go.layout.mapbox.Center(lat=48.8566, lon=2.3522), 
                                    zoom=1.),
                                    mapbox_style='open-street-map')

    )
])

# Run app
if __name__ == '__main__':
    app.run_server(debug=False)
