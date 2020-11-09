import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


ABOUT_PAGE = html.Div(
    [
    html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'TEAM 65',
                            className='row display-4 font-weight-bold justify-content-center font-medium',
                        ),
                    ],
                    className = 'container pt-5 mt-2'
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Img(src='/../assets/assets/photos_/IlanReinstein.jpeg', className='div-for-image-team',
                                            style={'height':'78%', 'width':'45%'}),
                                        html.Div('Ilan Reinstein', className='font-weight-bold text-names-team font-medium'),
                                        html.Div('-', className='text-subtitle-team'),

                                        html.Div(
                                            html.A(
                                                html.Img(src = '/../assets/assets/photos_/in_logo.png', style={'height': '5%', 'width':'5%'}),
                                                href='https://www.linkedin.com/in/ireinstein/', role="button",
                                            ),
                                            className='social',
                                        ),
                                    ],
                                    className='col div-for-member mx-4',
                                ),
                                html.Div(
                                    [
                                        html.Img(src='/../assets/photos_/DanielBorda.jpeg', className='div-for-image-team',
                                            style={'height':'78%', 'width':'45%'}),
                                        html.Div('Daniel Borda', className='font-weight-bold text-names-team font-medium'),
                                        html.Div('-', className='text-subtitle-team'),
                                        html.Div(
                                            html.A(
                                                html.Img(src = '/../assets/photos_/in_logo.png', style={'height': '5%', 'width':'5%'}),
                                                    href='https://www.linkedin.com/in/daniel-borda/', role="button",
                                            ),
                                            #className='social',
                                        ),
                                    ],
                                    className='col div-for-member mx-4',
                                ),
                            ],
                            className='row',
                        ),
                    ],
                    className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
                ),
            ],
            className = 'position-relative overflow-hidden text-center div-for-TEAM-65',
        ),

html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(src='/../assets/photos_/KaryHerrera.jpeg', className='div-for-image-team',
                                        style={'height':'82%', 'width':'78%'}),
                                    html.Div('Kary Herrera', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('-', className='text-subtitle-team'),

                                    html.Div(
                                        html.A(
                                            html.Img(src = '/../assets/photos_/in_logo.png', style={'height': '8%', 'width':'8%'}),
                                            href='https://www.linkedin.com/in/kary-alexandra-herrera-romero/', role="button",
                                        ),
                                        #className='social',
                                    ),
                                ],
                                className='col div-for-member mx-4',
                            ),
                            html.Div(
                                [
                                    html.Img(src='/../assets/photos_/DanielOtero.jpeg', className='div-for-image-team',
                                        style={'height':'82%', 'width':'78%'}),
                                    html.Div('Daniel Otero', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('-', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.Img(src = '/../assets/photos_/in_logo.png', style={'height': '8%', 'width':'8%'}),
                                                href='https://www.linkedin.com/in/daniel-otero-cárdenas/', role="button",
                                        ),
                                        #className='social',
                                    ),
                                ],
                                className='col div-for-member mx-4',
                            ),
                            html.Div(
                                [
                                    html.Img(src='/../assets/photos_/PaolaCruz.jpeg', className='div-for-image-team',
                                        style={'height':'82%', 'width':'78%'}),
                                    html.Div('Paola Cruz', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('-', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.Img(src = '/../assets/photos_/in_logo.png', style={'height': '8%', 'width':'8%'}),
                                                href='https://www.linkedin.com/in/paola-cruz-bol%C3%ADvar-1745bb125/', role="button",
                                        ),
                                        #className='social',
                                    ),
                                ],
                                className='col div-for-member mx-4',
                            ),
                        ],
                        className='row',
                    ),
                ],
                className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
            ),
        ],
        className = 'position-relative overflow-hidden text-center div-for-TEAM-65',
    ),

html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(src='/../assets/photos_/DiegoRojas.jpeg', className='div-for-image-team',
                                        style={'height':'80%', 'width':'45%'}),
                                    html.Div('Diego Rojas', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('-', className='text-subtitle-team'),

                                    html.Div(
                                        html.A(
                                            html.Img(src = '/../assets/photos_/in_logo.png', style={'height': '5%', 'width':'5%'}),
                                            href='https://www.linkedin.com/in/diego-alejandro-rojas-diaz-1a48b613a/', role="button",
                                        ),
                                        #className='social',
                                    ),
                                ],
                                className='col div-for-member mx-4',

                            ),
                            html.Div(
                                [
                                    html.Img(src='/../assets/photos_/CatalinaBernal.jpeg', className='div-for-image-team',
                                        style={'height':'80%', 'width':'45%'}),
                                    html.Div('Catalina Bernal', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('-', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.Img(src = '/../assets/photos_/in_logo.png', style={'height': '5%', 'width':'5%'}),
                                                href='https://www.linkedin.com/in/catalina-bernal-0612/', role="button",
                                        ),
                                        #className='social',
                                    ),
                                ],
                                className='col div-for-member mx-4',
                            ),
                        ],
                        className='row',
                    ),
                ],
                className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
            ),
        ],
        className = 'position-relative overflow-hidden text-center div-for-TEAM-65',
    ),
    ]
)
