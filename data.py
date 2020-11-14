"""
Data

Imports the data, cleans it and creates graphs according to what is needed. 
Additionally, here the dropdown lists are created
"""

import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
import pickle
import pickle
from sklearn.ensemble import GradientBoostingRegressor

"""
#  Importing data
"""

data = pd.read_csv('data_moda_description.csv', sep = ',')
data = data.rename(columns = {'precio': 'Price', 'dda':'quantity demanded'})
data_maps = pd.read_csv('campaign_with_departments.csv', sep = ',', encoding='latin-1')
data_maps = data_maps.rename(columns = {'article group': 'article_group'})

#Map info
with open('colombia_geo.json') as file:
    colombia_geo = json.load(file)

#Model
with open('model/config_dict.pkl', 'rb') as f:
    config_dict = pickle.load(f)
with open('model/gbm.pkl', 'rb') as f:
    model = pickle.load(f)
"""
#   Dropdowns
"""

dropdown_variables_spa = ['campaign', 'garment_type', 'article_group',
                     'section_mundo', 'clasificacion', 'pagina', 'num_apariciones', 'peso_exhibicion',
                     'TALLA_EDAD', 'color']
dropdown_variables_eng = ['Catalogue number', 'Type of clothing (Tipo Prenda)', 'Group of clothing',
                        'Section', 'Classification', 'Page number', 'Number of times shown on catalogue',
                        'Proportion of picture in page', 'Size group', 'Color']
dropdown_variables_id = list(range(len(dropdown_variables_eng)))
dropdown_variables = tuple(zip(dropdown_variables_spa, dropdown_variables_eng, dropdown_variables_id))



dropdown_group_desc_list = list(data['article_group'].unique())
dropdown_color_desc_list = list(data['color'].unique())
dropdown_size_desc_list = list(data['TALLA_EDAD'].unique())

dropdown_group_desc_list.append('All')
dropdown_color_desc_list.append('All')
dropdown_size_desc_list.append('All')

dropdown_group_fc_list = list(data['article_group'].unique())
dropdown_color_fc_list = list(data['color'].unique())
dropdown_size_fc_list = list(data['TALLA_EDAD'].unique())
dropdown_expo_type_fc_list = ['Modeled', 'Product photo', 'Modeled and product photo']
# dropdown_expo_type_fc_list = ['0-18 mo', '1-5 yo', '6-16 yo','other']
dropdown_gender_fc_list = ['Male', 'Female', 'Unisex']
dropdown_page_fc_list = ['{}-{}'.format(a,a+19) for a in range(0,81,20)]


"""
#  Functions for graphs
"""
#Graph (boxplot) that shows demand/price vs a selected variable
def boxplot_choose_variable(var_x, var_y = 'quantity demanded'):
    spa, eng, i = dropdown_variables[var_x]
    temp = data

    fig = px.box(temp, x = spa, y = var_y)
    fig.update_xaxes(title_text= eng)
    fig.update_yaxes(title_text='Demand (units)' if var_y == 'quantity demanded' else 'Price ($)')
    return fig

#Map of demand based on the selected group of the product
def map(group = 'All', type = 'D'):
    temp = data_maps
    groupby_vars = ['department']

    if group != 'All':
        temp = temp[temp['article_group'] == group]
        groupby_vars.append('article_group')

    if type == 'D':
        temp = temp.groupby(groupby_vars)['quantity demanded'].sum().reset_index()
        color_map = 'Viridis'
        var = 'quantity demanded'
    elif type == 'F':
        temp = temp.groupby(groupby_vars)['quantity invoiced'].sum().reset_index()
        color_map = 'Magma'
        var = 'quantity invoiced'
    else:
        raise Exception ('Something went wrong')
        return None

    # if group != 'All':
    #     temp = temp[temp['article_group'] == group]


    fig = px.choropleth_mapbox(temp,
                           geojson=colombia_geo,
                           locations=temp['department'],
                           featureidkey = 'properties.NOMBRE_DPT',
                           color=temp[var],
                           color_continuous_scale= color_map, #['white', 'orange', 'red'],
                           range_color= list(temp[var]), #.quantile([0,0.99])
                           mapbox_style="carto-positron",
                           zoom=4,
                           center = {"lat": 4.3634, "lon": -74.454},
                           opacity=0.5,
                          )
    fig.update_traces(zmax=temp[var].max(),zmin=temp[var].min())
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
    return fig

#Boxplot showing change in demand for a selected department throughout the months
def box_catalogue_department(group = 'All', department = 'All'):
    title = 'Demand vs catalogue number for {} in {}'.format('all groups' if group == 'All' else group, 'all departments' if department == 'All' else department)
    groupby_var = ['campaign']
    temp = data_maps 

    if (group != 'All') & (department != 'All'):
        groupby_var.extend(['article_group', 'department'])
        temp = temp.groupby(groupby_var)['quantity demanded'].sum().reset_index()
        temp = temp[(temp['article_group'] == group)]
        temp = temp[(temp['department'] == department)]
    elif (group != 'All'):
        groupby_var.extend(['article_group'])
        temp = temp.groupby(groupby_var)['quantity demanded'].sum().reset_index()
        temp = temp[(temp['article_group'] == group)]
    elif (department != 'All'):
        groupby_var.extend(['department'])
        temp = temp.groupby(groupby_var)['quantity demanded'].sum().reset_index()
        temp = temp[(temp['department'] == department)]
    else:
        temp = temp.groupby(groupby_var)['quantity demanded'].sum().reset_index()
    
    # fig = px.bar(temp, x = 'campaign', y = 'quantity demanded', title = title)
    fig = go.Figure(data=[go.Bar(
        x=temp['campaign'],
        y=temp['quantity demanded'],
        width=[0.8] * len(temp) # customize width here
    )])
    fig.update_xaxes(title_text = 'Catalogue number', tickvals = [i for i in range(1,9)])
    fig.update_yaxes(title_text = 'Demand (units)')
    fig.update_layout(title_text=title)
    return fig

#Graph to compare demand vs price for a selected group, color and size
def demand_vs_price(v1,v2,v3):
    temp = data

    if v1 != 'All':
        temp = temp[temp['article_group'] == v1]
    if v2 != 'All':
        temp = temp[temp['color'] == v2]
    if v3 != 'All':
        temp = temp[temp['TALLA_EDAD'] == v3]

    fig = px.scatter(temp, x = "Price", y = 'quantity demanded')
    # fig = px.density_heatmap(data, x = "PRECIO_CATALOGO", y = 'DDA_UND')
    fig.update_xaxes(title_text= "Price ($)")
    fig.update_yaxes(title_text='Demand (units)')
    return fig

"""
ML Model
"""
#As the model is in spanish, we had to mpa some of the inputs from english for the model to work correctly
def fun_user_input(precio_usuario,grupo_talla_usuario, tipo_item, color,exposicion_usuario, genero, expo_weight, rango_pagina):
    data_user = pd.DataFrame(columns=['z_price', 'zoom', 'expo_weight',
        'size_group_0-18 mo', 'size_group_1-5 yo', 'size_group_6-16 yo',
        'size_group_other', 'size_group_unisex', 'item_group_accesories',
        'item_group_bottoms', 'item_group_denim', 'item_group_full', 'item_group_tops',
        'color_Amarillo', 'color_Azul', 'color_Blanco', 'color_Café',
        'color_Gris', 'color_MIXTO', 'color_Morado', 'color_Naranja',
        'color_Negro', 'color_Rojo', 'color_Rosado', 'color_Verde',
        'gender_Femenino', 'gender_Masculino', 'gender_Otros', 'gender_Unisex',
        'expo_type_FOTO PRODUCTO', 'expo_type_MODELADO',
        'expo_type_MODELADO Y FOTO PRODUCTO', 'page_group_(0, 20]',
        'page_group_(20, 40]', 'page_group_(40, 60]', 'page_group_(60, 100]',
        'page_group_(100, 140]'])

    #create series used for predicting
    data_user = data_user.append(pd.Series(), ignore_index=True)
    data_user = data_user.fillna(0)

    #creates data
    data_user['z_price'] = (precio_usuario - 55796.48)/  22988.660

    if rango_pagina < 21:
        data_user['page_group_(0, 20]'] = 1
    elif rango_pagina < 41:
        data_user['page_group_(20, 40]'] = 1
    elif rango_pagina < 61:
        data_user['page_group_(40, 60]'] = 1
    elif rango_pagina < 101:
        data_user['page_group_(60, 100]'] = 1
    elif rango_pagina > 100:
        data_user['page_group_(100, 140]'] = 1

    if grupo_talla_usuario == '0 TO 24 MONTHS':
        data_user['size_group_0-18 mo'] = 1
    elif grupo_talla_usuario == '2 TO 5 YEARS':
        data_user['size_group_1-5 yo'] = 1
    elif grupo_talla_usuario == '6 TO 16 YEARS':
        data_user['size_group_6-16 yo'] = 1
    elif grupo_talla_usuario == 'NOT KNOWN':
        data_user['size_group_other'] = 1
    elif grupo_talla_usuario == 'UNISEX':
        data_user['size_group_unisex'] = 1

    if (tipo_item == 'T-SHIRT')   | (tipo_item == 'SWEATER OR JACKET')  | (tipo_item == 'SHIRT')  :
        data_user['item_group_tops'] = 1
    elif (tipo_item == 'LONG PANTS')   | (tipo_item == 'SHORTS')  | (tipo_item == 'SKIRT') :
        data_user['item_group_bottoms'] = 1
    elif (tipo_item == 'SET')   | (tipo_item == 'DRESS')  | (tipo_item == 'PAJAMA') | (tipo_item == 'OVERALL') | (tipo_item == 'BODY') | (tipo_item == 'OUTER SHIRT'):
        data_user['item_group_full'] = 1
    elif (tipo_item == 'ACCESSORY')   | (tipo_item == 'HAT') :
        data_user['item_group_accesories'] = 1
    elif (tipo_item == 'DENIM'):
        data_user['item_group_denim'] = 1

    if color == 'Yellow':
        data_user['color_Amarillo'] = 1
    elif color == 'Blue':
        data_user['color_Azul'] = 1
    elif color == 'White':
        data_user['color_Blanco'] = 1
    elif color == 'Brown':
        data_user['color_Café'] = 1
    elif color == 'Gray':
        data_user['color_Gris'] = 1
    elif color == 'Mix':
        data_user['color_MIXTO'] = 1
    elif color == 'Purple':
        data_user['color_Morado'] = 1
    elif color == 'Orange':
        data_user['color_Naranja'] = 1
    elif color == 'Black':
        data_user['color_Negro'] = 1
    elif color == 'Red':
        data_user['color_Rojo'] = 1
    elif color == 'Pink':
        data_user['color_Rosado'] = 1
    elif color == 'Green':
        data_user['color_Verde'] = 1

    if genero == 'Female':
        data_user['gender_Femenino'] = 1
    elif genero == 'Male':
        data_user['gender_Masculino'] = 1
    elif genero == 'Other':
        data_user['gender_Otros'] = 1
    elif genero == 'Unisex':
        data_user['gender_Unisex'] = 1

    if exposicion_usuario == 'Product photo':
        data_user['expo_type_FOTO PRODUCTO'] = 1
    elif exposicion_usuario == 'Modeled':
        data_user['expo_type_MODELADO'] = 1
    elif exposicion_usuario == 'Modeled and product photo':
        data_user['expo_type_MODELADO Y FOTO PRODUCTO'] = 1

        data_user['expo_weight'] = expo_weight

    return np.round(model.predict(data_user),0)