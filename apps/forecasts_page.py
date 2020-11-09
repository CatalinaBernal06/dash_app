import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_core_components.Loading import Loading
import dash_html_components as html

import data

##Precio, exposición, talla, campana, color

FORECASTS_PAGE = html.Div(
    [
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    html.H2(
                                        'Predict demand based on different variables', 
                                        style={
                                            'text-align': 'center'
                                        }
                                    ),
                                ),
                                style = {
                                    'vertical-align': 'top',
                                    'display': 'inline-block'
                                }
                            )
                        ]
                    ),
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
                            html.Div(
                                [
                                    html.H4(
                                        'Attention!'
                                    ),
                                    # html.Button(
                                    #     'X',
                                    #     className = 'close',
                                    #     **{
                                    #         'data-dismiss': 'alert'
                                    #     }
                                    # ),
                                    html.P(
                                        """
                                        For each of the boxes shown below, choose an option if it is a dropdown or insert a value if it is an input box. After selecting a value for
                                        each of the boxes, the prediction of the demand of the product with the selected features will be displayed below, along with its UPE.
                                        """,
                                        className = 'mb-0'
                                    )
                                ],
                                className = 'alert alert-dismissible alert-success',
                                style = {
                                    # 'margin-top': '5%'
                                }
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Price',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Input(
                                                        id = 'forecasts_price',
                                                        type = 'number',
                                                        placeholder = 'Insert product price',
                                                        style = {
                                                            'border':'1px solid #bec3c9', 
                                                            'width': '100%',
                                                            'height': '57.5%',
                                                        },
                                                    ),
                                                ],
                                                className = 'col-3',
                    
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Size',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Dropdown(
                                                        options=[
                                                            {'label': val, 'value': val} for val in data.dropdown_size_fc_list
                                                        ],
                                                        placeholder = 'Select',
                                                        id = 'forecasts_size'
                                                    ),
                                                ],
                                                className = 'col-3',

                                            ),
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Group',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Dropdown(
                                                        options=[
                                                            {'label': val, 'value': val} for val in data.dropdown_group_fc_list
                                                        ],
                                                        placeholder = 'Select',
                                                        id = 'forecasts_group'
                                                    ),
                                                ],
                                                className = 'col-3',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Color',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Dropdown(
                                                        options=[
                                                            {'label': val, 'value': val} for val in data.dropdown_color_fc_list
                                                        ],
                                                        placeholder = 'Select',
                                                        id = 'forecasts_color'
                                                    ),
                                                ],
                                                className = 'col-3',
                                            ),
                                        ]
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Exposition type',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Dropdown(
                                                        options=[
                                                            {'label': val, 'value': val} for val in data.dropdown_expo_type_fc_list
                                                        ],
                                                        placeholder = 'Select',
                                                        id = 'forecasts_expo_type'
                                                    ),
                                                ],
                                                className = 'col-3',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Gender',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Dropdown(
                                                        options=[
                                                            {'label': val, 'value': val} for val in data.dropdown_gender_fc_list
                                                        ],
                                                        placeholder = 'Select',
                                                        id = 'forecasts_gender'
                                                    ),
                                                ],
                                                className = 'col-3',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Exposition weight',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Input(
                                                        type = 'number',
                                                        placeholder = 'Insert exposition weight (between 0 and 1)',
                                                        style = {
                                                            'border':'1px solid #bec3c9', 
                                                            'width': '100%',
                                                            'height': '57.5%',
                                                        },
                                                        id = 'forecasts_expo_weight',
                                                        min = 0,
                                                        max = 1,
                                                        step = 0.01
                                                    ),
                                                ],
                                                className = 'col-3',
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H6(
                                                        'Page number',
                                                        style = {
                                                            'text-align': 'center'
                                                        }
                                                    ),
                                                    dcc.Dropdown(
                                                        options=[
                                                            {'label': val, 'value': val} for val in data.dropdown_page_fc_list
                                                        ],
                                                        placeholder = 'Select',
                                                        id = 'forecasts_page_number'
                                                    ),
                                                ],
                                                className = 'col-3',
                                            ),
                                        ]
                                    ),
                                ],
                                className = 'col-12'
                            ),
                        ]
                    ),
                    dbc.Row(
                        dbc.Col(
                            [
                                html.H6(
                                    'Select error margin',
                                    style = {
                                        'text-align': 'center'
                                    }
                                ),
                                dcc.Slider(
                                    min=0,
                                    max=1,
                                    step=None,
                                    value=0.5,
                                    marks = {
                                        (str(i/100) if i % 100 != 0 else str(int(i/100))): (str(i/100) if i % 10 == 0 else "") for i in range(0,101,5)
                                    },
                                    id = 'forecasts_slider'
                                ), 
                            ],
                            className = 'col-4'
                        ),
                    ),
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                                html.Button(
                                    'Run model',
                                    type = 'button',
                                    className = 'btn btn-outline-success',
                                    id = 'forecasts_run'
                                ),
                                style={
                                    'justify-content': 'center', 
                                    'display': 'flex',
                                }
                            ),
                            className = 'col-4'
                        ),
                        justify = 'center'
                    )
                ],
            ),
            className = 'jumbotron',
            style = {
                'margin-top': '10px'
            }
        ),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                html.Div(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Loading(
                                                        html.H1(
                                                            '10000',
                                                            id = 'forecast_demand_value',
                                                            style = {
                                                                'color': '#1DC72D',
                                                                'margin': '0',
                                                                'font-size': '150px'
                                                            }
                                                        ),
                                                    ),
                                                    className = 'col-3',
                                                    style = {
                                                        'display': 'flex',
                                                        'align-items': 'center',
                                                        'justify-content': 'center',
                                                        'padding-right': '0'
                                                    }
                                                ),
                                                dbc.Col(
                                                    html.H5(
                                                        'units demanded for the product with the selected characteristics',
                                                        style = {
                                                            'margin': '0'
                                                        }
                                                    ),
                                                    className = 'col-9',
                                                    style = {
                                                        'display': 'flex',
                                                        'align-items': 'center',
                                                        'justify-content': 'center',
                                                        'padding-left': '0'
                                                    }
                                                )
                                            ]
                                        )
                                    ],
                                    className = 'card-body',
                                    style = {
                                        'padding': '0'
                                    }
                                ),
                                className = 'card border-danger mb-3',
                            ),
                            className = 'col-6'
                        ),
                        dbc.Col(
                            html.Div(
                                html.Div(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Loading(
                                                        html.H1(
                                                            '0%',
                                                            id = 'forecast_upe_value',
                                                            style = {
                                                                'color': '#1DC72D',
                                                                'margin': '0',
                                                                'font-size': '150px'
                                                            }
                                                        ),
                                                    ),
                                                    className = 'col-3',
                                                    style = {
                                                        'display': 'flex',
                                                        'align-items': 'center',
                                                        'justify-content': 'center',
                                                        'padding-right': '0'
                                                    }
                                                ),
                                                dbc.Col(
                                                    html.H5(
                                                        'is the UPE for the product with the selected characteristics',
                                                        style = {
                                                            'margin': '0'
                                                        }
                                                    ),
                                                    className = 'col-9',
                                                    style = {
                                                        'display': 'flex',
                                                        'align-items': 'center',
                                                        'justify-content': 'center',
                                                        'padding-left': '0'
                                                    }
                                                )
                                            ]
                                        )
                                    ],
                                    className = 'card-body',
                                    style = {
                                        'padding': '0'
                                    }
                                ),
                                className = 'card border-danger mb-3',
                            ),
                            className = 'col-6'
                        )
                    ]
                ),
            ],
            className = 'jumbotron',
            style = {
                'margin-top': '10px'
            }
        )
    ]
)