from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from visualizations import plot_3d_scatter

# Load and preprocess data
data = pd.read_csv('migraine.csv')
data['Total_Sensory_Symptoms'] = data[['Dysphasia', 'Dysarthria', 'Vertigo', 'Tinnitus', 
                                       'Hypoacusis', 'Diplopia', 'Visual_defect', 'Paresthesia']].sum(axis=1)

# Initialize Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Migraine Sensory Symptoms Dashboard", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='chart-type',
        options=[
            {'label': '3D Scatter Plot', 'value': 'scatter_3d'}
        ],
        value='scatter_3d',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='main-graph')
])

# Callback to update graph
@app.callback(
    Output('main-graph', 'figure'),
    [Input('chart-type', 'value')]
)
def update_chart(chart_type):
    if chart_type == 'scatter_3d':
        return plot_3d_scatter(data)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
