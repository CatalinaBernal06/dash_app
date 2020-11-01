"""
Module doc string
"""
import dash
from dash_bootstrap_components._components.DropdownMenu import DropdownMenu
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

from apps.navbar import NAVBAR
from apps.home_page import HOME_PAGE
from apps.description_page import DESCRIPTION_PAGE
from apps.geographic_description import GEOGRAPHIC_DESCRIPTION_PAGE

import data


"""
#  Page Layout
"""
URL = dcc.Location(id = 'url', refresh = True)

BODY = html.Div(
    children = [],
    id = 'page_body'
)

"""
#  Create app
"""
app = dash.Dash(__name__)
# server = app.server  # for Heroku deployment
app.layout = html.Div(children=[NAVBAR, URL, BODY])


"""
#  Callbacks
"""
# Change layouts by pressing on tabs
@app.callback(
    [
        Output(component_id = 'Home_tab_list', component_property = 'className'),
        Output(component_id = 'Description_tab_list', component_property = 'className'),
        Output(component_id = 'Geographic_Description_tab_list', component_property = 'className'),
        Output(component_id = 'Forecasts_tab_list', component_property = 'className'),
        Output(component_id = 'About_tab_list', component_property = 'className'),
        Output(component_id='page_body', component_property='children')

    ],
    Input(component_id = 'url', component_property = 'pathname')
)

def description_tab(path):
    activated = 'nav-link active'
    not_activated = 'nav-link'
    if (path == '/') | (path == '/Home'):
        return activated, not_activated, not_activated, not_activated, not_activated, HOME_PAGE
    elif path == '/Description':
        return not_activated, activated, not_activated, not_activated, not_activated, DESCRIPTION_PAGE
    elif path == '/Geographic_Description':
        return not_activated, not_activated, activated, not_activated, not_activated, GEOGRAPHIC_DESCRIPTION_PAGE
    elif path == '/Forecasts':
        return not_activated, not_activated, not_activated, activated, not_activated, GEOGRAPHIC_DESCRIPTION_PAGE
    elif path == '/About':
        return not_activated, not_activated, not_activated, activated, HOME_PAGE

## Change demand graph depending on selected variable on dropdown
@app.callback(
    Output(component_id='graph_variable_demand', component_property='figure'),
    Input(component_id='dropdown_demand', component_property='value')
)
def set_graph_demand_choose_variable(val):
    return data.boxplot_choose_variable(val, 'DDA_UND')

## Change graph depending on selected variable on dropdown
@app.callback(
    Output(component_id='graph_variable_price', component_property='figure'),
    Input(component_id='dropdown_price', component_property='value')
)
def set_graph_price_choose_variable(val):
    return data.boxplot_choose_variable(val, 'PRECIO_CATALOGO')

"""
#  MAIN
"""
app.config['suppress_callback_exceptions'] = True
if __name__ == "__main__":
    app.run_server(debug=True)
 
