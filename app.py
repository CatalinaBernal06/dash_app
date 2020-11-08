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
from apps.forecasts_page import FORECASTS_PAGE
from apps.about_page import ABOUT_PAGE

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
server = app.server
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
        return not_activated, not_activated, not_activated, activated, not_activated, FORECASTS_PAGE
    elif path == '/About':
        return not_activated, not_activated, not_activated, not_activated, activated, ABOUT_PAGE

## Change demand graph depending on selected variable on dropdown
@app.callback(
    Output(component_id='graph_variable_demand', component_property='figure'),
    Input(component_id='dropdown_demand', component_property='value')
)
def set_graph_demand_choose_variable(val):
    return data.boxplot_choose_variable(val, 'quantity demanded')

## Change graph depending on selected variable on dropdown
@app.callback(
    Output(component_id='graph_variable_price', component_property='figure'),
    Input(component_id='dropdown_price', component_property='value')
)
def set_graph_price_choose_variable(val):
    return data.boxplot_choose_variable(val, 'Price')

## Change demand vs price graph depending on selected variable on dropdown
@app.callback(
    Output(component_id='graph_variable_demand_price', component_property='figure'),
    [
        Input(component_id='dropdown_group_desc', component_property='value'),
        Input(component_id='dropdown_color_desc', component_property='value'),
        Input(component_id='dropdown_size_desc', component_property='value'),
    ]
)
def set_graph_predict_choose_variable(v1,v2,v3):
    return data.demand_vs_price(v1,v2,v3)

#Click on map
@app.callback(
    [
        Output(component_id='map_label_selected', component_property='children'),
        Output(component_id='map_demand', component_property='figure'),
        Output(component_id='map_invoiced', component_property='figure'),
        Output(component_id='box_departments', component_property='figure'),
    ],
    [
        Input(component_id='map_demand', component_property='clickData'),
        Input(component_id='map_invoiced', component_property='clickData'),
        Input(component_id='dropdown_group_geo', component_property='value')
    ]
)
def select_box_table_geographic_description(demand_click, invoiced_click,dropdown):

    #Taken from https://dash.plotly.com/advanced-callbacks
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
        return 'Department: All', dash.no_update, dash.no_update, dash.no_update
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if (button_id == 'map_demand'):
            department = demand_click['points'][0]['location']
            return 'Department: ' + department, dash.no_update, dash.no_update, data.box_catalogue_department(dropdown, department)
        elif (button_id == 'map_invoiced'):
            department = invoiced_click['points'][0]['location']
            return 'Department: ' + department, dash.no_update, dash.no_update, data.box_catalogue_department(dropdown, department)
        elif button_id == 'dropdown_group_geo':
            return 'Department: All', data.map(dropdown), data.map(dropdown, type = 'F'), data.box_catalogue_department(dropdown)

#Run forecast
@app.callback(
    [
        Output(component_id='forecast_demand_value', component_property='children'),
        Output(component_id='forecast_upe_value', component_property='children'),
    ],
    Input(component_id='forecasts_run', component_property='n_clicks'),
    [
        State(component_id='forecasts_price', component_property='value'),
        State(component_id='forecasts_size', component_property='value'),
        State(component_id='forecasts_group', component_property='value'),
        State(component_id='forecasts_color', component_property='value'),
        State(component_id='forecasts_expo_type', component_property='value'),
        State(component_id='forecasts_gender', component_property='value'),
        State(component_id='forecasts_expo_weight', component_property='value'),
        State(component_id='forecasts_page_number', component_property='value'),
        State(component_id='forecasts_slider', component_property='value'),
    ]
)
def set_prediction_values(clicks, price, size, group, color, expo_type, gender, expo_weight, page_number, error_margin):
    if clicks == None:
        return '0','0'
    return "", ""
"""
#  MAIN
"""
app.config['suppress_callback_exceptions'] = True
if __name__ == "__main__":
    app.run_server(debug=True)
