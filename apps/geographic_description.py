import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import data
from data import box_catalogue_department

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
                                        'See how demand behaves throughout the country', 
                                        style={'text-align': 'center'}
                                    ),
                                ),
                                style = {
                                    'vertical-align': 'top',
                                    'display': 'inline-block'}
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
            [
                dbc.Row(
                    [
                        dbc.Col(
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
                                                'Select a group to visualize demand throughout the country. You can also click over a department on the map to show how demand changes over time in the plot below',
                                                className = 'mb-0'
                                            )
                                        ],
                                        className = 'alert alert-dismissible alert-success',
                                        style = {
                                            'margin-top': '15%'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                html.H4('Group of the product'),
                                                                className = 'col-4',
                                                                style = {
                                                                    'margin': 'auto'
                                                                }
                                                            ),
                                                            dbc.Col(
                                                                dcc.Dropdown(
                                                                    options=[
                                                                        {'label': val, 'value': val} for val in data.dropdown_group_desc_list
                                                                    ],
                                                                    value='All',
                                                                    id = 'dropdown_group_geo'
                                                                ),
                                                                # className = 'bg-primary',
                                                                style={
                                                                    # 'vertical-align': 'middle',
                                                                    'padding-top': '1%',
                                                                    # 'display': 'block',
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                    # html.Hr(
                                                    #     className = 'my-4'
                                                    # ),
                                                ],
                                                className = 'card-body'
                                            )
                                        ],
                                        className = 'card',
                                        style = {
                                            'margin-top': '5%'
                                        }
                                    ),
                                    
                                ],
                                className = 'col-4',
                            ),
                        dbc.Col(
                            [
                                html.H4(
                                    'Selected: All',
                                    id = 'map_label_selected'
                                ),
                                dcc.Loading(
                                        dcc.Graph(
                                            figure = data.box_catalogue_department(),
                                            id = 'box_departments'
                                        )
                                )
                            ],
                            className = 'col-8',
                        )
                    ]
                ),
            ],
            className = 'jumbotron'
        ),
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4(
                                        'Demand',
                                    ),
                                    dcc.Loading(
                                        dcc.Graph(
                                            figure = data.map(),
                                            id = 'map_demand'
                                        )
                                    ),
                                ],
                                className = 'col-6'
                            ),
                            dbc.Col(
                                [
                                    html.H4(
                                        'Invoiced',
                                    ),
                                    dcc.Loading(
                                        dcc.Graph(
                                            figure = data.map(type = 'F'),
                                            id = 'map_invoiced'
                                        )
                                    ),
                                ],
                                className = 'col-6'
                            ),
                        ]
                    ),
                ],
            ),
            className = 'jumbotron',
            style = {
                'max-width': '90%'
            }
        ),
    ]
)