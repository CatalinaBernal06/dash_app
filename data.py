import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
#import sqlalchemy

"""
#  Importing data
"""

data = pd.read_csv('data_moda_description.csv', sep = ',')
data = data.rename(columns = {'precio': 'Price', 'dda':'quantity demanded'})
data_maps = pd.read_csv('campaign_with_departments.csv', sep = ',', encoding='latin-1')
data_maps = data_maps.rename(columns = {'article group': 'article_group'})

with open('colombia_geo.json') as file:
    colombia_geo = json.load(file)

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
dropdown_expo_type_fc_list = ['None', 'Modeled', 'Product photo', 'Modeled and product photo']
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