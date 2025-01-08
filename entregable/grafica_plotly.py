import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.offline as pyo

df = pd.read_csv('Tratados_internacionales_de_Colombia_20241206.csv')

columna1 = df['Lugar de Adopcion'][-20:]
columna2 = df['Fecha de Adopcion'][-20:]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=columna2,
        y=columna1,
        mode='lines+markers',
        line=dict(color='red', width=3, dash='dash'),
        marker=dict(size=10, color='orange', symbol='circle'),
        name='Datos de Adopción'
    )
)

fig.update_layout(
    title=dict(
        text="Gráfica de Tratados de Adopcion",
        font=dict(size=24, color='darkblue'),
        x=0.5  
    ),
    xaxis=dict(
        title='Fechas',
        titlefont=dict(size=18, color='gray'),
        tickangle=45,
        showgrid=True,
        gridcolor='lightgray'
    ),
    yaxis=dict(
        title='Ciudades',
        titlefont=dict(size=18, color='gray'),
        showgrid=True,
        gridcolor='lightgray'
    ),
    plot_bgcolor='white',
    paper_bgcolor='whitesmoke',
    legend=dict(
        title='Leyenda',
        font=dict(size=14)
    )
)
fig.show()

