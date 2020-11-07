import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
#import sqlalchemy

"""
#  Importing data
"""

# pwd = 'DS4A'
# user = 'offcorss'
# database ='offcorss'
# host = 'data-offcorss.cirlxddueyc2.us-east-2.rds.amazonaws.com'
# port = 5432
# conn = sqlalchemy.create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{database}')

# query = """SELECT sku_plu, campaign, clasificacion, garment_type, color_comercial, codigo_color, talla, article_group, SUM(quantity demanded) as quantity demanded, SUM(fac_und) as fac, AVG(precio_catalogo) as precio, AVG(upe_D) as upe
# FROM campanas
# WHERE clasificacion = 'Moda'
# GROUP BY sku_plu, campaign, clasificacion, garment_type, color_comercial, codigo_color, talla, article_group;"""

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

data = pd.read_csv('data_moda.csv', sep = ',')
data = data.rename(columns = {'precio': 'Price', 'dda':'quantity demanded'})
data_maps = pd.read_csv('campaign_with_departments.csv', sep = ',', encoding='latin-1')

with open('colombia_geo.json') as file:
    colombia_geo = json.load(file)

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


"""
#  Functions for graphs
"""
def boxplot_choose_variable(var_x, var_y = 'quantity demanded'):
    spa, eng, i = dropdown_variables[var_x]
    temp = data

    fig = px.box(temp, x = spa, y = var_y)
    fig.update_xaxes(title_text= eng)
    fig.update_yaxes(title_text='Demand (units)' if var_y == 'quantity demanded' else 'Price ($)')
    return fig

def map(group, type = 'D'):
    if type == 'D':
        temp = data_maps.groupby(['department', 'article group'])['quantity demanded'].sum().reset_index()
    elif type == 'P':
        temp = data_maps.groupby(['department', 'article group'])['catalog_price'].mean().reset_index()
    else:
        raise Exception ('Something went wrong')
        return None

    temp = temp[temp['article group'] == group]
    fig = px.choropleth_mapbox(temp,
                           geojson=colombia_geo,
                           locations=temp['department'],
                           featureidkey = 'properties.NOMBRE_DPT',
                           color=temp['quantity demanded'],
                           color_continuous_scale=['white', 'orange', 'red'], #Viridis
                           range_color= list(temp['quantity demanded'].quantile([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])),
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
#         temp = temp[temp['article_group'] == v1]
#     if v2 != 'All':
#         temp = temp[temp['color'] == v2]
#     if v3 != 'All':
#         temp = temp[temp['TALLA_EDAD'] == v3]
#
#     fig = px.scatter(temp, x = "PRECIO_CATALOGO", y = 'quantity demanded')
#     # fig = px.density_heatmap(data, x = "PRECIO_CATALOGO", y = 'quantity demanded')
#     fig.update_xaxes(title_text= "Price ($)")
#     fig.update_yaxes(title_text='Demand (units)')
#     return fig

def demand_catalogue_predict(v1,v2,v3):
    temp = data

    if v1 != 'All':
        temp = temp[temp['article_group'] == v1]
    if v2 != 'All':
        temp = temp[temp['color'] == v2]
    if v3 != 'All':
        temp = temp[temp['TALLA_EDAD'] == v3]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = [1,2 ,3, 4, 5, 6, 7, 8],
            y=[sum(temp[temp.campaign==1]['quantity demanded']), sum(temp[temp.campaign==2]['quantity demanded']), sum(temp[temp.campaign==3]['quantity demanded'])
            ,sum(temp[temp.campaign==4]['quantity demanded']), sum(temp[temp.campaign==5]['quantity demanded']), sum(temp[temp.campaign==6]['quantity demanded']),
            sum(temp[temp.campaign==7]['quantity demanded']), sum(temp[temp.campaign==8]['quantity demanded'])], name = 'Time Series', marker = dict(color = 'gold')
            #mode = 'lines+markers+text', text = ty03, textposition = 'top right', textfont = dict(family='overpass',
            #size = 14, color = 'rgb(254,178,76)')
            ))

    fig.add_trace(
        go.Bar(
            x=[1,2 ,3, 4, 5, 6, 7, 8],
            y=[sum(temp[temp.campaign==1]['quantity demanded']), sum(temp[temp.campaign==2]['quantity demanded']), sum(temp[temp.campaign==3]['quantity demanded'])
            ,sum(temp[temp.campaign==4]['quantity demanded']), sum(temp[temp.campaign==5]['quantity demanded']), sum(temp[temp.campaign==6]['quantity demanded']),
            sum(temp[temp.campaign==7]['quantity demanded']), sum(temp[temp.campaign==8]['quantity demanded'])], name = 'Bar Plot', marker = dict(color = 'dodgerblue'),
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
        temp = temp[(temp['article group'] == group)]
    if department != 'All':
        temp = temp[(temp['department'] == department)]
    fig = px.box(temp, x = 'campaign', y = 'quantity demanded', title = title)
    fig.update_xaxes(title_text = 'Catalogue number')
    fig.update_yaxes(title_text = 'Demand (units)')
    return fig
