"""
Home page

Contains a short summary of the company and the problem.
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

OC_LOGO = 'https://img.kupino.co/kupi/loga_shopy/offcorss.png'

HOME_PAGE = html.Div(
     [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
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
                                        # className = 'border border-primary'
                                    ),
                                    href = 'https://www.offcorss.com/?ProductLinkNotFound=ropa-bebe-nina-faldas-y-shorts-short-4205283&gclid=CjwKCAjwz6_8BRBkEiwA3p02VcU8Tad5Rz8WCeCCnH0_1v3xiY2y1CvxG-1KejPGnM1MN7wOSFBDzxoCp2cQAvD_BwE'
                                ),
                                style = {
                                    'width': 4,
                                    'justify-content': 'center',
                                    'vertical-aling': 'upper',
                                    'display': 'flex',
                                    # 'padding': '0 0 5% 0'
                                },
                                # className = 'border border-primary'
                            )
                        )
                    ],
                    style = {
                         'width': 6
                    }
                ),
                dbc.Col(
                    [
                        dbc.Row(
                                html.Div(
                                         [
                                          html.P(
                                                 """
                                                     C. I HERMECO S.A is the
                                                     market leader in clothing for the children's segment in Colombia. They identify themselves as a
                                                     company with 40 years of experience, committed to offer authentic, reliable and fun products
                                                     and experiences for kids with diverse lifestyles. They always seek to exceed the satisfaction of
                                                     their customers and guarantee the durability of the company.

                                                     """,
                                                 className='lead font-weight-normal text-dark font-home-m', style = {'text-align':'justify', 'padding': '20px 50px 10px 0'}
                                                 ),

                                          html.P(
                                                 """

                                                     The high number of references they work on a monthly basis makes it difficult to make a forecast
                                                     fitting the reality of the distribution channels, in specific, catalogue distribution. Using historical data, we will try to predict the
                                                     number of units to be produced for each reference at the catalogue distribution channel.
                                                     """,
                                                 className='lead font-weight-normal text-dark font-home-m', style = {'text-align':'justify', 'padding': '20px 50px 30px 0'}
                                                 ),

                                        #  html.A('See more about Catalogue Distribution here', className='btn btn-outline-primary text-dark font-home-m',
                                        #     href='https://ventadirecta.offcorss.com/', style = {'text-align':'center'})#, 'padding': '20px 50px 30px 0'})

                                          ],
                                        #  className='mb-5',
                                        ),
                             ),

                    ],
                    width = {
                        'size': 6,
                    },
                        ),

            ],
            justify = 'center',
            style = {
                'margin': '25px',
            }
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    html.A(
                        'See more about Catalogue Distribution here',
                        className='btn btn-outline-warning',
                        href='https://ventadirecta.offcorss.com/', 
                        style = {
                            'text-align':'center'
                        }
                    ),
                ),
                style={
                    'justify-content': 'center', 
                    'display': 'flex',
                }
            ),
            justify = 'center',
            style = {
                'margin-top': 0
            }
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                            html.A(
                                html.Img(
                                    src='/../assets/photos_/corr_one_2.jpeg',
                                    style = {
                                        'height':'100px',
                                        'padding-left': '20%'
                                    },
                                ),
                                href = 'https://www.correlation-one.com/'
                            ),
                        ),
                        className = 'col-4',
                ),
                dbc.Col(
                    html.Div(
                            html.A(
                                html.Img(
                                    src='/../assets/photos_/mintic_logo.jpeg',
                                    style = {
                                        'height': '100px',
                                        'padding-left': '25%'
                                    },
                                ),
                                href = 'https://www.mintic.gov.co/portal/inicio/'
                            ),
                        ),
                    className = 'col-4',

                ),
            ],
            style = {
                'margin-top': '4%'
            }
        ),
    ],
)
