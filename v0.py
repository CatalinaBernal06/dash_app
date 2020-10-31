"""
Module doc string
"""
from datetime import datetime
import dash
from dash_bootstrap_components._components.DropdownMenu import DropdownMenu
import dash_table
# import matplotlib.colors as mcolors
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input, State
import random
import folium
import json

"""
#  Functions for data
"""
def preprocessing(df):
    ##Sizes
    df.loc[df['MUNDO'] == 'Niña', 'TALLA_EDAD'] = '6 a 16 años' 
    df.loc[df['MUNDO'] == 'Niño', 'TALLA_EDAD'] = '6 a 16 años' 
    df.loc[df['MUNDO'] == 'Bebé Niño', 'TALLA_EDAD'] = '2 a 5 años' 
    df.loc[df['MUNDO'] == 'Bebé Niña', 'TALLA_EDAD'] = '2 a 5 años' 
    df.loc[df['MUNDO'] == 'bebé niño', 'TALLA_EDAD'] = '2 a 5 años' 
    df.loc[df['MUNDO'] == 'bebé niña', 'TALLA_EDAD'] = '2 a 5 años' 
    df.loc[df['MUNDO'] == 'Primi Niña', 'TALLA_EDAD'] = '0 a 24 meses' 
    df.loc[df['MUNDO'] == 'Primi Niño', 'TALLA_EDAD'] = '0 a 24 meses' 
    df.rename(columns={'DDA UND': 'DDA_UND'}, inplace=True)
    ## colours
    def agrupar_color(color):
#     s = ''.jo==(re.f==dall('[A-Za-z]', color))
        s = color
        if  ('Azul' == s) | ('Gris' == s) | ('Rosado'  == s) | ('Café' == s)  | ('Morado' == s)  | ('Amarillo'  == s)  | ('Blanco' == s) | ('Verde'  == s)  | ('Negro'  == s)   | ('Rojo' == s) | ('Naranja'  == s)  :
            return s
        elif ('Índigo Medio' == s) | ('Índigo Claro' == s) | ('Indigo negro' == s) | ('Índigo'  == s)  | ('Indigo Claro'  == s) |  ('Indigo Oscuro'  == s)  |  ('Azul rayas'  == s)  |  ('Turquesa'  == s)  |  ('Indigo Medio'  == s) :
            return 'Azul'
        elif ('Coral' == s) | ('Rosado/ Estampado' == s):
            return 'Rosado'
        elif ('plateado' == s) | ('gris' == s)  | ('Gris Jaspe' == s) | ('Gris jaspe' == s)      :
            return 'Gris'
        elif ('caf' == s):
            return 'Café'
        elif ('Violeta' == s) | ('Fucsia' == s):
            return 'Morado'
        elif ('Mostaza' == s) | ('Arena' == s) :
            return 'Amarillo'
        elif   ('Blanco /Estampado' == s) | ('Beige' == s) :
            return 'Blanco'
        elif ('Camuflado' == s)  |  ('Verde Neón'  == s)    :
            return 'Verde'
        elif ('S== REGISTRO' == s):
            return 'S== Dato'   
        else:
            return  'MIXTO'
    df["COLOR_COME_AGRUP"] = df['COLOR_COMERCIAL'].apply(agrupar_color)
    ##Return
    return df

def preprocessing_maps(df):
    df.rename(columns={'DEPARTAMENTO ': "DEPARTAMENTO"}, inplace=True)
    df.rename(columns={'CAMPAÃA': "CAMPANA"}, inplace=True)
    df.rename(columns={'DDA UND': "DDA_UND"}, inplace=True)
    return df

"""
#  Functions for graphs
"""
def boxplot_choose_variable(var_x, var_y = 'DDA_UND'):
    spa, eng, i = dropdown_variables[var_x]
    fig = px.box(data, x = spa, y = var_y)
    fig.update_xaxes(title_text= eng)
    fig.update_yaxes(title_text='Demand (units)' if var_y == 'DDA_UND' else 'Price ($)')
    return fig

def map(group, type = 'D'):
    if type == 'D':
        temp = data_maps.groupby(['DEPARTAMENTO', 'GRUPO_ARTICULO'])['DDA_UND'].sum().reset_index()
    elif type == 'P':
        temp = data_maps.groupby(['DEPARTAMENTO', 'GRUPO_ARTICULO'])['PRECIO_CATALOGO'].mean().reset_index()
    else:
        raise Exception ('Something went wrong')
        return None
    temp = temp[temp['GRUPO_ARTICULO'] == group]
    fig = px.choropleth_mapbox(temp, 
                           geojson=colombia_geo, 
                           locations=temp['DEPARTAMENTO'],
                           featureidkey = 'properties.NOMBRE_DPT',
                           color=temp['DDA_UND'],
                           color_continuous_scale="Viridis",
                           range_color= list(temp['DDA_UND'].quantile([0, 0.25, 0.5, 0.75, 1])),
                           mapbox_style="carto-positron",
                           zoom=4, center = {"lat": 4.3634, "lon": -74.454},
                           opacity=0.5
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
    return fig

"""
#  Importing data
"""
OC_LOGO = 'https://img.kupino.co/kupi/loga_shopy/offcorss.png'

data = pd.read_csv('campaign_matrix_with_region.csv', sep = ',')
data = preprocessing(data)
data_maps = pd.read_csv('campaign_matrix_with_region_1.csv', sep = ',', encoding='latin-1')
data_maps = preprocessing_maps(data_maps)
with open('colombia_geo.json') as file:
    colombia_geo = json.load(file)

dropdown_variables_spa = ['CAMPAÑA', 'TIPO PRENDA', 'GRUPO_ARTICULO', 
                    'REGION', 'MUNDO', 'CLASIFICACIÓN', '# PÁGINA', 'NUM_ APARICIONES', 'PESO_ EXHIBICIÓN',
                     'TALLA_EDAD', 'COLOR_COME_AGRUP']
dropdown_variables_eng = ['Catalogue number', 'Type of clothing (Tipo Prenda)', 'Group of clothing (Grupo Artículo)',
                        'Region', 'Section (Mundo)', 'Clasification', 'Page Number', 'Number of times shown on catalogue', 
                        'Proportion of item in page', 'Size', 'Color']
dropdown_variables_id = list(range(len(dropdown_variables_eng)))
dropdown_variables = tuple(zip(dropdown_variables_spa, dropdown_variables_eng, dropdown_variables_id))


"""
#  Navigation Bar
"""

NAVBAR = dbc.Navbar(
    children = [
        ###
        ### Navbar Brand
        ###
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    # dbc.Col(html.Img(src=OC_LOGO, style={'height':'50px', 'width':'50px'}))
                    dbc.Col(dbc.NavbarBrand('OFFCORSS', className = 'navbar-brand'))
                ],
                align="center",
                no_gutters=True,
            ),
            className = '"navbar-brand'
        ),
        html.Button(
            html.Span(
                className = 'navbar-toggler-icon'
            ),
            className = 'navbar-toggler',
            type = 'button',
            **{
                'data-toggle': 'collapse',
                'data-target': '#navbarColor01',
                'aria-controls': "navbarColor01",
                'aria-expanded': "false",
                'aria-label': "Toggle navigation"
                }
        ),
        ###
        ### Options
        ###
        html.Div(
            html.Ul(
                children = [
                    html.Li(
                        html.A(
                            children = [
                                'Home',
                                html.Span(
                                    '(current)',
                                    className = 'sr-only'
                                )
                            ],
                            className = 'nav-link',
                            href="Home",
                            id = 'Home_tab'
                        ),
                        className = 'nav-item',
                        id ='Home_tab_list'
                    ),
                    html.Li(
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            'Description',
                            className = 'nav-link',
                            href="Description",
                            id = 'Description_tab'
                        ),
                        className = 'nav-item',
                        id = 'Description_tab_list'
                    ),
                    html.Li(
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            'Geographic Description',
                            className = 'nav-link',
                            href="Geographic_Description",
                            id = 'Geographic_Description_tab'
                        ),
                        className = 'nav-item',
                        id = 'Geographic_Description_tab_list'
                    ),
                    html.Li(
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            'Forecasts',
                            className = 'nav-link',
                            href="Forecasts",
                            id = 'Forecasts_tab'
                        ),
                        className = 'nav-item',
                        id = 'Forecasts_tab_list'
                    ),
                    html.Li(
                        html.A(
                            # Use row and col to control vertical alignment of logo / brand
                            'About',
                            className = 'nav-link',
                            href="About",
                            id = 'About_tab'
                        ),
                        className = 'nav-item',
                        id = 'About_tab_list'
                    ),
                    # html.Li(
                    #     html.A(
                    #         children = [
                    #             'Dropdown',
                    #             html.Div(
                    #                 children = [
                    #                     html.A(
                    #                         'Action',
                    #                         className = 'dropdown-item'
                    #                     ),
                    #                     html.A(
                    #                         'Action #2',
                    #                         className = 'dropdown-item'
                    #                     )
                    #                 ],
                    #                 className = 'dropdown-menu',
                    #                 id = 'dropdown_list'
                    #             ),
                    #         ],
                    #         className = 'nav-link dropdown-toggle',
                    #         href="#1",
                    #         role = 'button',
                    #         id = 'input_dropdown',
                    #         **{
                    #             'data-toggle': "dropdown",
                    #             'aria-haspopup': "true",
                    #             'aria-expanded': "false"
                    #         }
                    #     ),
                    #     # dbc.DropdownMenu(
                    #         # children = [
                    #     #         dbc.DropdownMenuItem('hola'),
                    #     #         dbc.DropdownMenuItem('hola2')
                    #     #     ],
                    #     #     label = 'Dropdown',
                    #     #     className = 'nav-link dropdown-toggle',
                    #     # ),
                    #     # className = 'nav-item dropdown'
                    # ),
                ],
                className = 'navbar-nav mr-auto'
            ),
            className = 'collapse navbar-collapse'
        ),
    ],
    className = 'navbar navbar-expand-lg navbar-dark bg-primary'
)

"""
#  Page Layout
"""
URL = dcc.Location(id = 'url', refresh = True)

HOME_PAGE = html.Div(
    children = [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            html.A(
                                html.Img(
                                    src=OC_LOGO, 
                                    style = {
                                        # 'vertical-align': 'middle',
                                        # 'margin-left': 'auto',
                                        # 'margin-right': 'auto',
                                        # 'display': 'block',
                                        'height':'100%'
                                    },
                                    className = 'border border-primary'
                                ),
                                href = 'https://www.offcorss.com/?ProductLinkNotFound=ropa-bebe-nina-faldas-y-shorts-short-4205283&gclid=CjwKCAjwz6_8BRBkEiwA3p02VcU8Tad5Rz8WCeCCnH0_1v3xiY2y1CvxG-1KejPGnM1MN7wOSFBDzxoCp2cQAvD_BwE'
                            ),
                            style = {
                                'width': 6,
                                'justify-content': 'center',
                                'vertical-aling': 'middle',
                                'display': 'flex',
                                # 'padding': '0 0 5% 0'
                            },
                            className = 'border border-primary'
                        )
                    ],
                    style = {
                        'width': 6,
                        'justify-content': 'center',
                        'display': 'flex',
                    },
                    className = 'column'
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                # html.Div(
                                                #     'Header 1',
                                                #     className = 'card-header'
                                                # ),
                                                html.Div(
                                                    [
                                                        html.H4(
                                                            'Description',
                                                            className = 'card-title'
                                                        ),
                                                        html.P(
                                                            'Characterization of demand and price compared to variables of your choice (only 2020)',
                                                            className = 'card-text'
                                                        ),
                                                        html.A(
                                                            html.Button(
                                                                'Take me there',
                                                                className = 'btn btn-primary btn-sm',
                                                                type = 'button',
                                                            ),
                                                            href = 'Description'
                                                        ),
                                                    ],
                                                    className = 'card-body',
                                                )
                                            ],
                                            className = 'card bg-secondary mb-3',
                                            style = {
                                                'max-width': '20rem',
                                            }
                                        )
                                    ],   
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                # html.Div(
                                                #     'Header 2',
                                                #     className = 'card-header'
                                                # ),
                                                html.Div(
                                                    [
                                                        html.H4(
                                                            'Demand seen geographically',
                                                            className = 'card-title'
                                                        ),
                                                        html.P(
                                                            'See how demand and price behave throughout the country',
                                                            className = 'card-text'
                                                        ),
                                                        html.A(
                                                            html.Button(
                                                                'Take me there',
                                                                className = 'btn btn-primary btn-sm',
                                                                type = 'button',
                                                            ),
                                                            href = 'Geographic_Description'
                                                        ),
                                                    ],
                                                    className = 'card-body'
                                                )
                                            ],
                                            className = 'card bg-secondary mb-3',
                                            style = {
                                                'max-width': '20rem'
                                            }
                                        )
                                    ],   
                                )
                            ],
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                # html.Div(
                                                #     'Header 3',
                                                #     className = 'card-header'
                                                # ),
                                                html.Div(
                                                    [
                                                        html.H4(
                                                            'Forecasts',
                                                            className = 'card-title'
                                                        ),
                                                        html.P(
                                                            'Predict demand based on different variables, including ones from the catalogue',
                                                            className = 'card-text'
                                                        ),
                                                        html.A(
                                                            html.Button(
                                                                'Take me there',
                                                                className = 'btn btn-primary btn-sm',
                                                                type = 'button',
                                                            ),
                                                            href = 'Forecasts'
                                                        ),
                                                    ],
                                                    className = 'card-body'
                                                )
                                            ],
                                            className = 'card bg-secondary mb-3',
                                            style = {
                                                'max-width': '20rem'
                                            }
                                        )
                                    ],   
                                ),
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                # html.Div(
                                                #     'Header 4',
                                                #     className = 'card-header'
                                                # ),
                                                html.Div(
                                                    [
                                                        html.H4(
                                                            'About',
                                                            className = 'card-title'
                                                        ),
                                                        html.P(
                                                            'Know more about the creators of this project',

                                                            className = 'card-text'
                                                        ),
                                                        html.Br(),
                                                        html.A(
                                                            html.Button(
                                                                'Take me there',
                                                                className = 'btn btn-primary btn-sm',
                                                                type = 'button',
                                                            ),
                                                            href = 'About'
                                                        ),
                                                    ],
                                                    className = 'card-body'
                                                )
                                            ],
                                            className = 'card bg-secondary mb-3',
                                            style = {
                                                'max-width': '20rem'
                                            }
                                        )
                                    ],   
                                )
                            ],
                        ),
                    ],
                    width = {
                        'size': 6,
                    },
                )
            ],
            justify = 'center',
            style = {
                'margin': '100px',
            }
        )
    ],
)

DESCRIPTION_PAGE = html.Div(
    [
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    html.H2(
                                        'Select whether you want to visualize all data or only for classification "Moda"', 
                                        style={'text-align': 'center'}
                                    ),
                                ),
                                style = {
                                    'vertical-align': 'top',
                                    'display': 'inline-block'}
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Button(
                                    'Hello its me', 
                                    className = 'btn btn-outline-warning active',
                                    style = {'width': '80%'}
                                    ),
                                ],
                                style={
                                    'width': 4, 
                                    'justify-content': 'center', 
                                    'display': 'flex'
                                    }
                            ),
                            dbc.Col(
                                [
                                    html.Button(
                                    'Hello its me', 
                                    className = 'btn btn-outline-warning',
                                    style = {'width': '80%'}
                                    ),
                                ],
                                style={
                                    'width': 4, 
                                    'justify-content': 'center', 
                                    'display': 'flex'
                                    }
                            )
                        ],
                        justify = 'center'
                    )
                ],
            ),
            className = 'jumbotron',
            style = {
                'max-width': '90%'
            }
        ),
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3(
                                    'Choose a variable to compare against demand'
                                )
                            ),
                            dbc.Col(
                                dcc.Dropdown(
                                    options=[
                                       {'label': eng, 'value': i} for spa, eng, i in dropdown_variables
                                    ],
                                    value=0,
                                    id = 'dropdown_demand'
                                ),
                                className = 'col'
                            )
                        ],
                        className = 'row'
                    ),
                    dbc.Row(
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    id = 'graph_variable_demand'
                                ),
                            )
                        )
                    )
                ],
            ),
            className = 'jumbotron',
            style = {
                'max-width': '90%'
            }
        ),
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3(
                                    'Choose a variable to compare against price'
                                )
                            ),
                            dbc.Col(
                                dcc.Dropdown(
                                    options=[
                                       {'label': eng, 'value': i} for spa, eng, i in dropdown_variables
                                    ],
                                    value=1,
                                    id = 'dropdown_price'
                                )
                            )
                        ],
                    ),
                    dbc.Row(
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    id = 'graph_variable_price',
                                ),
                            )
                        )
                    )
                ],
            ),
            className = 'jumbotron',
        )
    ],
)

GEOGRAPHIC_DESCRIPTION_PAGE = html.Div(
    [
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    html.H2(
                                        'Select whether you want to visualize all data or only for classification "Moda"', 
                                        style={'text-align': 'center'}
                                    ),
                                ),
                                style = {
                                    'vertical-align': 'top',
                                    'display': 'inline-block'}
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Button(
                                    'Hello its me', 
                                    className = 'btn btn-outline-warning active',
                                    style = {'width': '80%'}
                                    ),
                                ],
                                style={
                                    'width': 4, 
                                    'justify-content': 'center', 
                                    'display': 'flex'
                                    }
                            ),
                            dbc.Col(
                                [
                                    html.Button(
                                    'Hello its me', 
                                    className = 'btn btn-outline-warning',
                                    style = {'width': '80%'}
                                    ),
                                ],
                                style={
                                    'width': 4, 
                                    'justify-content': 'center', 
                                    'display': 'flex'
                                    }
                            )
                        ],
                        justify = 'center'
                    )
                ],
            ),
            className = 'jumbotron',
            style = {
                'max-width': '90%'
            }
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    html.Div(
                                        dcc.Dropdown(
                                            options=[
                                                {'label': eng, 'value': i} for spa, eng, i in dropdown_variables
                                            ],
                                            value=0,
                                            style = {
                                                'border': 'None'
                                            }
                                        ),
                                    )
                                )
                            ],
                            className = 'col-3',
                        ),
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    figure = map('CAMISA')
                                )
                            ),
                            className = 'col-9',
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    figure = map('CAMISA')
                                )
                            ),
                        ),
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    figure = map('CAMISETA')
                                )
                            ),
                        )
                    ],
                )
            ],
            className = 'jumbotron'
        )
    ]

)

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
    return boxplot_choose_variable(val, 'DDA_UND')

## Change graph depending on selected variable on dropdown
@app.callback(
    Output(component_id='graph_variable_price', component_property='figure'),
    Input(component_id='dropdown_price', component_property='value')
)
def set_graph_price_choose_variable(val):
    return boxplot_choose_variable(val, 'PRECIO_CATALOGO')

"""
#  MAIN
"""
app.config['suppress_callback_exceptions'] = True
if __name__ == "__main__":
    app.run_server(debug=True)
 
