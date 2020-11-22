from collections import namedtuple
import numpy as np
import altair as alt
import math
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

"""
# PANTHER's AO algorithm

The AO algorithm allows you to ....


"""

"""
##### Input and Data
"""

units = st.selectbox(
    "In what units will you be providing spatial measurements",
    ("centimeters ", "millimeters", "meters"),
)

"""
######
"""

Acc1X1X2X3 = st.text_input(
    "Provide Accelerometer #1's location by inputting the values of its x-,y-, and z-coordinates separated by commas. For example in somple global co-ordinates frame the x-,y-, and z-cordinates of the Acceleroemeter #1 is 0.2 cm, 5 cm, 3.2 cm, then in the followsing box input 0.2, 5, 3.2",
    "0.0,0.0,0.0",
    1000,
    "Acc1X1X2X3Key",
)


Acc2X1X2X3 = st.text_input(
    "Provide Accelerometer #2's x-,y-, and z-coordinates separated by commas.",
    "0.0,0.0,0.0",
    1000,
    "Acc2X1X2X3Key",
)

Acc3X1X2X3 = st.text_input(
    "Provide Accelerometer #3's x-,y-, and z-coordinates separated by commas.",
    "0.0,0.0,0.0",
    1000,
    "Acc3X1X2X3Key",
)


Acc4X1X2X4 = st.text_input(
    "Provide Accelerometer #4's x-,y-, and z-coordinates separated by commas.",
    "0.0,0.0,0.0",
    1000,
    "Acc4X1X2X3Key",
)
# Acc1X2 = st.text_input("y-coordintate", "0.0", 10, "Acc1X2Key")
# Acc1X3 = st.text_input("z-coordintate", "0.0", 10, "Acc1X1Key")


Measurement1_numpy = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
Measurement2_numpy = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
Measurement3_numpy = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
Measurement4_numpy = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

DataFile1 = st.file_uploader("Measurements from Accelerometer 1 ")
if DataFile1 is not None:
    Measurement1_df = pd.read_csv(DataFile1)
    Measurement1_numpy = Measurement1_df.to_numpy()
    st.line_chart(Measurement1_df.rename(columns={"x": "index"}).set_index("index"))


DataFile2 = st.file_uploader("Measurements from Accelerometer 2 ")
if DataFile2 is not None:
    Measurement2_df = pd.read_csv(DataFile2)
    Measurement2_numpy = Measurement2_df.to_numpy()
    st.line_chart(Measurement2_df.rename(columns={"x": "index"}).set_index("index"))
DataFile3 = st.file_uploader("Measurements from Accelerometer 3 ")
if DataFile3 is not None:
    Measurement3_df = pd.read_csv(DataFile3)
    Measurement3_numpy = Measurement3_df.to_numpy()
    st.line_chart(Measurement3_df.rename(columns={"x": "index"}).set_index("index"))
DataFile4 = st.file_uploader("Measurements from Accelerometer 4 ")
if DataFile4 is not None:
    Measurement4_df = pd.read_csv(DataFile4)
    Measurement4_numpy = Measurement4_df.to_numpy()
    st.line_chart(Measurement4_df.rename(columns={"x": "index"}).set_index("index"))


"""
### The average value of the Accelerometer \#1's acceleration is
"""
dummy = np.array(Measurement1_numpy[:, 0])
st.write(np.average(dummy))

# """
# ### y column
# """
# st.write(Measurement1_numpy[:, 1])
#

fig, ax = plt.subplots()
if DataFile1 is not None and DataFile2 is not None:
    ax.plot(Measurement1_numpy[:, 1], Measurement2_numpy[:, 1])
    st.pyplot(fig)

"""
#### Contributors:
 * [The PANTHER program](https://www.panther.engr.wisc.edu/)
 * [Applied Mechanics Lab](https://appliedmechanicslab.github.io/)



#### AO-agorithm publication
###### Access from
* [Applied Mechanics Lab (preprint, free access, pdf)](https://appliedmechanicslab.github.io/AnAccelerometer-onlyAlgorithm.pdf)
* [arXiv.org, preprint (preprint, free access, pdf)](https://arxiv.org/abs/1911.09556)
* [Journal of the Mechanics and Physics of Solids (final version, pdf) ](https://www.sciencedirect.com/science/article/pii/S0022509620302490?casa_token=IMQbF22_LLQAAAAA:1JB4y48vk3JLYflI500eIczbVXQ9zyyLRpvQ84t_dLv8dlShY8MKkmFxovwYtW3xabOWfIy9M8g)
"""
