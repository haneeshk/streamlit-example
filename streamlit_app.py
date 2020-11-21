from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to the first app from Applied Mechanics Lab!
In the meantime, below is an example of what you can do with just a few lines of code:
"""

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
     bytes_data = uploaded_file.read()
     st.write(bytes_data)

# x= bytes_data[:,1]
# y=bytes_data[:,2]

df = pd.DataFrame({

  'date': ['10/1/2019','10/2/2019', '10/3/2019', '10/4/2019'],
  'second column': [10, 20, 30, 40]
})

df

st.line_chart(df.rename(columns={'date':'index'}).set_index('index'))

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
