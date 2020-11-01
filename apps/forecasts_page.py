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
                                html.Div(
                                    html.H2(
                                        'Predict demand based on different variables', 
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
            html.Div(
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
                                                'Select a group, color and size of a piece of clothing to predict demand. You can also choose the error margin for the UPE with the slider below the graph',
                                                className = 'mb-0'
                                            )
                                        ],
                                        className = 'alert alert-dismissible alert-success',
                                        style = {
                                            # 'margin-top': '5%'
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
                                                                    id = 'dropdown_group_desc'
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
                                                    html.Hr(
                                                        className = 'my-4'
                                                    ),
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                html.H4('Color'),
                                                                className = 'col-4',
                                                                style = {
                                                                    'margin': 'auto'
                                                                }
                                                            ),
                                                            dbc.Col(
                                                                dcc.Dropdown(
                                                                    options=[
                                                                        {'label': val, 'value': val} for val in data.dropdown_color_desc_list
                                                                    ],
                                                                    value='All',
                                                                    id = 'dropdown_color_desc'
                                                                    # style = {
                                                                    #     'padding': '10% 10%',
                                                                    #     'width': '100%'
                                                                    # }
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
                                                    html.Hr(
                                                        className = 'my-4'
                                                    ),
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                html.H4('Size'),
                                                                className = 'col-4',
                                                                style = {
                                                                    'margin': 'auto'
                                                                }
                                                            ),
                                                            dbc.Col(
                                                                dcc.Dropdown(
                                                                    options=[
                                                                        {'label': val, 'value': val} for val in data.dropdown_size_desc_list
                                                                    ],
                                                                    value='All',
                                                                    id = 'dropdown_size_desc'
                                                                    # style = {
                                                                    #     'padding': '10% 10%',
                                                                    #     'width': '100%'
                                                                    # }
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
                                                    html.Hr(
                                                        className = 'my-4'
                                                    ),
                                                ],
                                                className = 'card-body'
                                            )
                                        ],
                                        className = 'card',
                                        style = {
                                            # 'margin-top': '5%'
                                        }
                                    ),
                                ],
                                className = 'col-4',
                            ),
                            dbc.Col(
                                [
                                    dcc.Loading(
                                        dcc.Graph(
                                            id = 'graph_variable_demand_price',
                                        ),
                                    ),
                                    html.Div(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        html.H5('Select error margin for UPE'),
                                                        className = 'col-4'
                                                    ),
                                                    dbc.Col(
                                                        dcc.Slider(
                                                            min=0,
                                                            max=1,
                                                            step=None,
                                                            value=0.5,
                                                            marks = {
                                                                (str(i/100) if i % 100 != 0 else str(int(i/100))): (str(i/100) if i % 10 == 0 else "") for i in range(0,101,5)
                                                            }
                                                        ),
                                                        className = 'col-8'
                                                    ),
                                                ],
                                                className = 'row',
                                                style = {
                                                    # 'padding-top': '3%'
                                                }
                                            ),
                                        ],
                                        className = 'card',
                                        style = {
                                            'margin-top': '2%'
                                        }
                                    ),
                                ],
                                className = 'col-8'
                            )
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H5('Card 1')
                                    ],
                                    className = 'card'
                                ),
                                className = 'col-2'
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H5('Card 2')
                                    ],
                                    className = 'card'
                                ),
                                className = 'col-2'
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H5('Card 3')
                                    ],
                                    className = 'card'
                                ),
                                className = 'col-2'
                            ),
                            dbc.Col(
                                html.Div(
                                    [
                                        html.H5('Card 4')
                                    ],
                                    className = 'card'
                                ),
                                className = 'col-2'
                            )
                        ],
                        justify = 'center'
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
