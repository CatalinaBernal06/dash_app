import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import data

FORECASTS_PAGE = html.Div(
    [
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3(
                                    'Forecasting'
                                )
                            ),
                            # dbc.Col(
                            #     dcc.Dropdown(
                            #         options=[
                            #            {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                            #         ],
                            #         value=1,
                            #         id = 'dropdown_demand_price'
                            #     )
                            # )
                        ],
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            html.H5('Number of months ahead'),
                                                            className = 'col-4',
                                                            style = {
                                                                'margin': 'auto'
                                                            }
                                                        ),
                                                        dbc.Col(
                                                            dcc.Dropdown(
                                                                options=[
                                                                    {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                                                                ],
                                                                value=1,

                                                            ),
                                                            # className = 'bg-primary',
                                                            style={
                                                                'padding-top': '1%',
                                                            }
                                                        )
                                                    ],
                                                    style = {
                                                        'margins-bottom': '1px'
                                                    }
                                                ),
                                                html.Hr(
                                                    className = 'my-4'
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            html.H5('Group of clothing'),
                                                            className = 'col-4',
                                                            style = {
                                                                'margin': 'auto'
                                                            }
                                                        ),
                                                        dbc.Col(
                                                            dcc.Dropdown(
                                                                options=[
                                                                    {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                                                                ],
                                                                value=1,
                                                            ),
                                                            # className = 'bg-primary',
                                                            style={
                                                                'padding-top': '1%',
                                                            }
                                                        )
                                                    ],
                                                    style = {
                                                        'margins-bottom': '1px'
                                                    }
                                                ),
                                                html.Hr(
                                                    className = 'my-4'
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            html.H5('Group of clothing'),
                                                            className = 'col-4',
                                                            style = {
                                                                'margin': 'auto'
                                                            }
                                                        ),
                                                        dbc.Col(
                                                            dcc.Dropdown(
                                                                options=[
                                                                    {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                                                                ],
                                                                value=1,

                                                            ),
                                                            # className = 'bg-primary',
                                                            style={
                                                                'padding-top': '1%',
                                                            }
                                                        )
                                                    ],
                                                    style = {
                                                        'margins-bottom': '1px'
                                                    }
                                                ),
                                                html.Hr(
                                                    className = 'my-4'
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            html.H5('Group of clothing'),
                                                            className = 'col-4',
                                                            style = {
                                                                'margin': 'auto'
                                                            }
                                                        ),
                                                        dbc.Col(
                                                            dcc.Dropdown(
                                                                options=[
                                                                    {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                                                                ],
                                                                value=1,

                                                            ),
                                                            # className = 'bg-primary',
                                                            style={
                                                                'padding-top': '1%',
                                                            }
                                                        )
                                                    ],
                                                    style = {
                                                        'margins-bottom': '1px'
                                                    }
                                                ),
                                                html.Hr(
                                                    className = 'my-4'
                                                ),
                                            ],
                                            className = 'card-body'
                                        )
                                    ],
                                    className = 'card'
                                ),
                                className = 'col-4'
                            ),
                            dbc.Col(
                                dcc.Loading(
                                    dcc.Graph(
                                        id = 'graph_variable_demand_price',
                                    ),
                                )
                            )
                        ]
                    )
                ],
            ),
            className = 'jumbotron',
            style = {
                'margin-top': '10px'
            }
        )
    ]
)