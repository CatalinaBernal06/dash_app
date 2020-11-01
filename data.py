import pandas as pd
import json
import plotly.express as px


# host = 'data-offcorss.cirlxddueyc2.us-east-2.rds.amazonaws.com'
# port = 5432
# user = 'offcorss'
# database = 'offcorss'
# password = 'DS4A'
#
# condb = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
# connect = condb.raw_connection()
# cur = connect.cursor()
#
#
# """
# #   Fetchall tables from queries
# """
#
# test_cam = pd.read_sql("SELECT * FROM campanas",condb)
#
# test_cat = pd.read_sql("SELECT * FROM catalogo",condb)
#
# ## Agrupar color
# def agrupar_color(color):
#     s = color
#     if  ('Azul' == s) | ('Gris' == s) | ('Rosado'  == s) | ('Café' == s)  | ('Morado' == s)  | ('Amarillo'  == s)  | ('Blanco' == s) | ('Verde'  == s)  | ('Negro'  == s)   | ('Rojo' == s) | ('Naranja'  == s)  :
#         return s
#     elif  ('Azul Flores' == s) | ('Azul Dinosaurio' == s) |  ('Azul León' == s) | ('Índigo Medio' == s) | ('Índigo Claro' == s) | ('Azul con estrellas' == s) | ('Indigo negro' == s) | ('Índigo'  == s)  | ('Indigo Claro'  == s) |  ('Indigo Oscuro'  == s)  |  ('Azul rayas'  == s)  |  ('Turquesa'  == s)  |  ('Indigo Medio'  == s) :
#         return 'Azul'
#     elif ('Coral' == s) | ('Rosado/ Estampado' == s) | ('coral neon' == s):
#         return 'Rosado'
#     elif ('Gris Perro' == s) | ('Gris Koala' == s) | ('plateado' == s) | ('gris' == s)  | ('Gris Jaspe' == s) | ('Gris Gato' == s)  | ('Gris militar' == s) | ('Gris jaspe' == s) | ('Gris Oso' == s) | ('Gris Tiburón' == s) | ('Gris Estrellas' == s)  | (' Gris militar' == s)       :
#         return 'Gris'
#     elif ('Cafe' == s) | ('Café Gorila' == s) | ('Café León'== s)  :
#         return 'Café'
#     elif ('Violeta' == s) | ('Fucsia' == s):
#         return 'Morado'
#     elif ('Mostaza' == s) | ('Arena' == s) :
#         return 'Amarillo'
#     elif  ('Negro con letra' == s) | ('Negro Cocodrilo' == s) :
#         return 'Negro'
#     elif   ('Rosado Cerdito' == s) | ('Rosado Tigre' == s)  | ('Rosado Perro' == s)   :
#         return 'Rosado'
#     elif ('Naranja Tigre' == s) :
#         return 'Naranja'
#     elif   ('Blanco /Estampado' == s) | ('Beige' == s) | ('Blanco Conejo' == s) | ('Blanco Zorro' == s) :
#         return 'Blanco'
#     elif ('Camuflado' == s)  |  ('Verde Neón'  == s)    :
#         return 'Verde'
#     elif ('S== REGISTRO' == s):
#         return 'S== Dato'
#     else:
#         return  'MIXTO'
#
# ## Filter demand zero
# def filter_campaign(dat):
#     zero_demand = (dat['dda_und'] == 0) & (dat['fac_und'] != 0)
#     return dat[~zero_demand].copy()
#
#
# campaign_valid = filter_campaign(test_cam)
#
# moda = campaign_valid.merge(test_cat, left_on='sku_plu', right_on='plu', how ='inner')
# moda['color'] = moda['color_comercial'].apply(agrupar_color)
#
# moda['color'] = moda['color'].replace({'Azul': 'Blue', 'Gris':'Gray', 'Rosado':'Pink',
#         'Café':'Brown', 'Morado':'Purple', 'Amarillo':'Yellow', 'Blanco': 'White',
#         'Verde':'Green', 'Negro': 'Black', 'Rojo':'Red', 'Naranja': 'Orange', 'MIXTO': 'Mix'})
#
# data = moda.drop_duplicates(subset='plu', keep ='first').set_index('plu')
#
# #data = pd.read_csv('campaign_matrix_with_region.csv', sep = ',')
# data_maps = pd.read_sql(
#     'SELECT * FROM dep',
#     con=condb,
#     parse_dates=[
#         'created_at',
#         'updated_at'
#     ]
# )


"""
#  Importing data
"""

data = pd.read_csv('campaign_matrix_with_region.csv', sep = ',')
data_maps = pd.read_csv('campaign_matrix_with_region_1.csv', sep = ',', encoding='latin-1')

with open('colombia_geo.json') as file:
    colombia_geo = json.load(file)

dropdown_variables_spa = ['CAMPAÑA', 'TIPO PRENDA', 'GRUPO_ARTICULO',
                    'REGION', 'MUNDO', 'CLASIFICACIÓN', '# PÁGINA', 'NUM_ APARICIONES', 'PESO_ EXHIBICIÓN',
                     'TALLA_EDAD', 'COLOR_COME_AGRUP']
dropdown_variables_eng = ['Catalogue number', 'Type of clothing (Tipo Prenda)', 'Group of clothing (Grupo Artículo)',
                        'Region', 'Section (Mundo)', 'Clasification', 'Page Number', 'Number of times shown on catalogue',
                        'Proportion of item in page', 'Size', 'Color']
dropdown_variables_id = list(range(len(dropdown_variables_eng)))
dropdown_variables = tuple(zip(dropdown_variables_spa, dropdown_variables_eng, dropdown_variables_id))

"""
#  Functions for data
"""
def preprocessing(df):
    ##Sizes
    df.loc[df['MUNDO'] == 'Niña', 'TALLA_EDAD'] = '6 a 16 años'
    df.loc[df['MUNDO'] == 'Niño', 'TALLA_EDAD'] = '6 a 16 años'
    df.loc[df['MUNDO'] == 'Bebé Niño', 'TALLA_EDAD'] = '2 a 5 años'
    df.loc[df['MUNDO'] == 'Bebé Niña', 'TALLA_EDAD'] = '2 a 5 años'
    df.loc[df['MUNDO'] == 'bebé niño', 'TALLA_EDAD'] = '2 a 5 años'
    df.loc[df['MUNDO'] == 'bebé niña', 'TALLA_EDAD'] = '2 a 5 años'
    df.loc[df['MUNDO'] == 'Primi Niña', 'TALLA_EDAD'] = '0 a 24 meses'
    df.loc[df['MUNDO'] == 'Primi Niño', 'TALLA_EDAD'] = '0 a 24 meses'
    df.rename(columns={'DDA UND': 'DDA_UND'}, inplace=True)
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

data = preprocessing(data)
data_maps = preprocessing_maps(data_maps)


"""
#  Functions for graphs
"""
def boxplot_choose_variable(var_x, var_y = 'DDA_UND'):
    spa, eng, i = dropdown_variables[var_x]
    fig = px.box(data, x = spa, y = var_y)
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
                           color_continuous_scale="Viridis",
                           range_color= list(temp['DDA_UND'].quantile([0, 0.25, 0.5, 0.75, 1])),
                           mapbox_style="carto-positron",
                           zoom=4, center = {"lat": 4.3634, "lon": -74.454},
                           opacity=0.5
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
    return fig
