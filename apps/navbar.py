"""
Navbar

Bar at the top of the page. Contains all of the pages that the user can go to
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

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
