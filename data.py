import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
#import sqlalchemy

"""
#  Functions for data
"""
def preprocessing(df):
    ##Sizes
    df.loc[df['MUNDO'] == 'Niña', 'TALLA_EDAD'] = '6 to 16 years'
    df.loc[df['MUNDO'] == 'Niño', 'TALLA_EDAD'] = '6 to 16 years'
    df.loc[df['MUNDO'] == 'Bebé Niño', 'TALLA_EDAD'] = '2 to 5 years'
    df.loc[df['MUNDO'] == 'Bebé Niña', 'TALLA_EDAD'] = '2 to 5 years'
    df.loc[df['MUNDO'] == 'bebé niño', 'TALLA_EDAD'] = '2 to 5 years'
    df.loc[df['MUNDO'] == 'bebé niña', 'TALLA_EDAD'] = '2 to 5 years'
    df.loc[df['MUNDO'] == 'Primi Niña', 'TALLA_EDAD'] = '0 to 24 months'
    df.loc[df['MUNDO'] == 'Primi Niño', 'TALLA_EDAD'] = '0 to 24 months'
    df.loc[pd.isna(df['MUNDO']), 'TALLA_EDAD'] = 'Not Known'
    df.rename(columns={'DDA UND': 'DDA_UND'}, inplace=True)
    # df = df.astype({'PLU': object, '# PÁGINA': object})
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
        elif ('plateado' == s) | ('gris' == s)  | ('Gris Jaspe' == s) | ('Gris jaspe' == s):
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
#  Importing data
"""

# pwd = 'DS4A'
# user = 'offcorss'
# database ='offcorss'
# host = 'data-offcorss.cirlxddueyc2.us-east-2.rds.amazonaws.com'
# port = 5432
# conn = sqlalchemy.create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{database}')

# query = """SELECT sku_plu, campaign, clasificacion, tipo_prenda, color_comercial, codigo_color, talla, grupo_articulo, SUM(dda_und) as dda, SUM(fac_und) as fac, AVG(precio_catalogo) as precio, AVG(upe_D) as upe
# FROM campanas
# WHERE clasificacion = 'Moda'
# GROUP BY sku_plu, campaign, clasificacion, tipo_prenda, color_comercial, codigo_color, talla, grupo_articulo;"""

# sql_camp = pd.read_sql(
#     query,
#     con=conn,
#     parse_dates=[
#         'created_at',
#         'updated_at'
#     ]
# )

# data_maps = pd.read_sql(
#     'SELECT * FROM dep',
#     con=conn,
#     parse_dates=[
#         'created_at',
#         'updated_at'
#     ]
# )

# camp = pd.read_sql(
#     'SELECT * FROM catalogo',
#     con=conn,
#     parse_dates=[
#         'created_at',
#         'updated_at'
#     ]
# )

data = pd.read_csv('campaign_matrix_with_region.csv', sep = ',')
data_maps = pd.read_csv('campaign_matrix_with_region_1.csv', sep = ',', encoding='latin-1')

with open('colombia_geo.json') as file:
    colombia_geo = json.load(file)

dropdown_variables_spa = ['CAMPAÑA', 'TIPO PRENDA', 'GRUPO_ARTICULO',
                    'REGION', 'MUNDO', 'CLASIFICACIÓN', '# PÁGINA', 'NUM_ APARICIONES', 'PESO_ EXHIBICIÓN',
                     'TALLA_EDAD', 'COLOR_COME_AGRUP']
dropdown_variables_eng = ['Catalogue number', 'Type of clothing (Tipo Prenda)', 'Group of clothing (Grupo Artículo)',
                        'Region', 'Section (Mundo)', 'Classification', 'Page number', 'Number of times shown on catalogue',
                        'Proportion of picture in page', 'Size', 'Color']
dropdown_variables_id = list(range(len(dropdown_variables_eng)))
dropdown_variables = tuple(zip(dropdown_variables_spa, dropdown_variables_eng, dropdown_variables_id))

data = preprocessing(data)
data['COLOR_COME_AGRUP'] = data['COLOR_COME_AGRUP'].replace({'Azul': 'Blue', 'Gris':'Gray', 'Rosado':'Pink',
        'Café':'Brown', 'Morado':'Purple', 'Amarillo':'Yellow', 'Blanco': 'White',
        'Verde':'Green', 'Negro': 'Black', 'Rojo':'Red', 'Naranja': 'Orange', 'MIXTO': 'Mix'})
data_maps = preprocessing_maps(data_maps)

dropdown_group_desc_list = list(data['GRUPO_ARTICULO'].unique())
dropdown_color_desc_list = list(data['COLOR_COME_AGRUP'].unique())
dropdown_size_desc_list = list(data['TALLA_EDAD'].unique())

dropdown_group_desc_list.append('All')
dropdown_color_desc_list.append('All')
dropdown_size_desc_list.append('All')

data['random_predict'] = np.random.randint(1, 5, len(data))
"""
#  Functions for graphs
"""
def boxplot_choose_variable(var_x, var_y = 'DDA_UND'):
    spa, eng, i = dropdown_variables[var_x]
    temp = data

    fig = px.box(temp, x = spa, y = var_y)
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
                           color_continuous_scale=['white', 'orange', 'red'], #Viridis
                           range_color= list(temp['DDA_UND'].quantile([0, 0.25, 0.5, 0.75, 1])),
                           mapbox_style="carto-positron",
                           zoom=4.25,
                           center = {"lat": 4.3634, "lon": -74.454},
                           opacity=0.5,
                          )
    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
        )
    # fig.update_layout(legend_title_text = 'Demand')
    return fig

# def demand_vs_price(v1,v2,v3):
#     temp = data
#
#     if v1 != 'All':
#         temp = temp[temp['GRUPO_ARTICULO'] == v1]
#     if v2 != 'All':
#         temp = temp[temp['COLOR_COME_AGRUP'] == v2]
#     if v3 != 'All':
#         temp = temp[temp['TALLA_EDAD'] == v3]
#
#     fig = px.scatter(temp, x = "PRECIO_CATALOGO", y = 'DDA_UND')
#     # fig = px.density_heatmap(data, x = "PRECIO_CATALOGO", y = 'DDA_UND')
#     fig.update_xaxes(title_text= "Price ($)")
#     fig.update_yaxes(title_text='Demand (units)')
#     return fig

def demand_catalogue_predict(v1,v2,v3):
    temp = data

    if v1 != 'All':
        temp = temp[temp['GRUPO_ARTICULO'] == v1]
    if v2 != 'All':
        temp = temp[temp['COLOR_COME_AGRUP'] == v2]
    if v3 != 'All':
        temp = temp[temp['TALLA_EDAD'] == v3]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = [1,2 ,3, 4, 5, 6, 7, 8],
            y=[sum(temp[temp.CAMPAÑA==1].DDA_UND), sum(temp[temp.CAMPAÑA==2].DDA_UND), sum(temp[temp.CAMPAÑA==3].DDA_UND)
            ,sum(temp[temp.CAMPAÑA==4].DDA_UND), sum(temp[temp.CAMPAÑA==5].DDA_UND), sum(temp[temp.CAMPAÑA==6].DDA_UND),
            sum(temp[temp.CAMPAÑA==7].DDA_UND), sum(temp.random_predict)], name = 'Time Series', marker = dict(color = 'gold')
            #mode = 'lines+markers+text', text = ty03, textposition = 'top right', textfont = dict(family='overpass',
            #size = 14, color = 'rgb(254,178,76)')
            ))

    fig.add_trace(
        go.Bar(
            x=[1,2 ,3, 4, 5, 6, 7, 8],
            y=[sum(temp[temp.CAMPAÑA==1].DDA_UND), sum(temp[temp.CAMPAÑA==2].DDA_UND), sum(temp[temp.CAMPAÑA==3].DDA_UND)
            ,sum(temp[temp.CAMPAÑA==4].DDA_UND), sum(temp[temp.CAMPAÑA==5].DDA_UND), sum(temp[temp.CAMPAÑA==6].DDA_UND),
            sum(temp[temp.CAMPAÑA==7].DDA_UND), sum(temp.random_predict)], name = 'Bar Plot', marker = dict(color = 'dodgerblue'),
            hoverinfo='none'
            ))

    fig.update_xaxes(title_text= "Catalogue Number")
    fig.update_yaxes(title_text='Demand (units)')
    fig.update_layout(showlegend=False)
    return fig

def box_catalogue_department(group = 'All',department = 'All'):
    title = 'Demand vs catalogue number for {} in {}'.format('all groups' if group == 'All' else group, 'all departments' if department == 'All' else department)
    temp = data_maps
    if group != 'All':
        temp = temp[(temp['GRUPO_ARTICULO'] == group)]
    if department != 'All':
        temp = temp[(temp['DEPARTAMENTO'] == department)]
    fig = px.box(temp, x = 'CAMPANA', y = 'DDA_UND', title = title)
    fig.update_xaxes(title_text = 'Catalogue number')
    fig.update_yaxes(title_text = 'Demand (units)')
    return fig
