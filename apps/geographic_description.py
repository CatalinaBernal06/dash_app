import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import data

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
                                                {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
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
                                    figure = data.map('CAMISA')
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
                                    figure = data.map('CAMISA')
                                )
                            ),
                        ),
                        dbc.Col(
                            dcc.Loading(
                                dcc.Graph(
                                    figure = data.map('CAMISETA')
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