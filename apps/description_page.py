import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import data

dropdown_group_desc_list = list(data.data['GRUPO_ARTICULO'].unique())
dropdown_color_desc_list = list(data.data['COLOR_COME_AGRUP'].unique())
dropdown_size_desc_list = list(data.data['TALLA_EDAD'].unique())

dropdown_group_desc_list.append('All')
dropdown_color_desc_list.append('All')
dropdown_size_desc_list.append('All')

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
                                    'ONLY MODA', 
                                    className = 'btn btn-outline-warning active',
                                    style = {'width': '80%'},
                                    id = 'button_moda_desc'
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
                                    'ALL DATA', 
                                    className = 'btn btn-outline-warning',
                                    style = {'width': '80%'},
                                    id = 'button_all_desc'
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
                                       {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                                    ],
                                    value=0,
                                    id = 'dropdown_demand'
                                ),
                                className = 'col',
                                
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
                                       {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
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
        ),
        dbc.Container(
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3(
                                    'Demand / Price comparison for a given product'
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
                                                            html.H4('Group of the product'),
                                                            className = 'col-4',
                                                            style = {
                                                                'margin': 'auto'
                                                            }
                                                        ),
                                                        dbc.Col(
                                                            dcc.Dropdown(
                                                                options=[
                                                                    {'label': val, 'value': val} for val in dropdown_group_desc_list
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
                                                                    {'label': val, 'value': val} for val in dropdown_color_desc_list
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
                                                                    {'label': val, 'value': val} for val in dropdown_size_desc_list
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
                                                # html.Div(
                                                #     [
                                                #         html.H4('hey'),
                                                #         dcc.Dropdown(
                                                #             options=[
                                                #                 {'label': eng, 'value': i} for spa, eng, i in data.dropdown_variables
                                                #             ],
                                                #             value=1
                                                #         ),
                                                #     ]
                                                # ),
                                                html.Hr(
                                                    className = 'my-4'
                                                ),
                                            ],
                                            className = 'card-body'
                                        )
                                    ],
                                    className = 'card',
                                    style = {
                                    'margin-top': '5%'
                                }
                                ),
                                className = 'col-4',
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
        )
    ],
)