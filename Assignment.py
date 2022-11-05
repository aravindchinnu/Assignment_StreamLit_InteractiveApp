import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

Maths = pd.read_csv('Maths.csv')

st.write(Maths)

st.sidebar.header("Pick the type of plot and variables for which you want to see the plot")

plot_type = st.sidebar.selectbox('Select your plot type', ['Scatter', 'Bar', 'Line','Histogram'])

if plot_type == 'Histogram':
    x_var = st.sidebar.selectbox("Pick your variable for which you want to plot histogram",Maths.select_dtypes(include = np.number).columns.tolist())
else:
    x_var = st.sidebar.selectbox("Pick your X-Axis",Maths.select_dtypes(include = np.number).columns.tolist())
    y_var = st.sidebar.selectbox("Pick your Y-Axis",Maths.select_dtypes(include = np.number).columns.tolist())
    corr = round(Maths[x_var].corr(Maths[y_var]),2)
    st.write(f"correlation between {x_var} and {y_var} is {corr}")

st.header('Visualizations are shown here')

if plot_type == 'Scatter':
    scatter = alt.Chart(Maths,title = f"Correlation between {x_var} and {y_var}").mark_point(size = 100,opacity=0.9).encode(
    alt.X(x_var,title = f"{x_var}"),
    alt.Y(y_var,title = f"{y_var}"), 
    tooltip=[x_var,y_var]).properties(width=500, height=500)
    st.altair_chart(scatter.interactive(), use_container_width=True)
elif plot_type == 'Bar':
    bar = alt.Chart(Maths,title = f"Correlation between {x_var} and {y_var}").mark_bar(size = 100,opacity=0.9).encode(
    alt.X(x_var,title = f"{x_var}"),
    alt.Y(y_var,title = f"{y_var}"), 
    tooltip=[x_var,y_var]).properties(width=500, height=500)
    st.altair_chart(bar.interactive(), use_container_width=True)
elif plot_type == 'Line':
    line = alt.Chart(Maths,title = f"Correlation between {x_var} and {y_var}").mark_line(size = 100,opacity=0.9).encode(
    alt.X(x_var,title = f"{x_var}"),
    alt.Y(y_var,title = f"{y_var}"), 
    tooltip=[x_var,y_var]).properties(width=500, height=500)
    st.altair_chart(line.interactive(), use_container_width=True)
elif plot_type == 'Histogram':
    bar = alt.Chart(Maths,title = f"Histogram of {x_var} ").mark_bar(size = 100,opacity=0.9).encode(
    alt.X(x_var,title = f"{x_var}"),
    y = 'count()', 
    tooltip=[x_var]).properties(width=500, height=500)
    st.altair_chart(bar.interactive(), use_container_width=True)