
# %%
# imports plugins
import pandas as pd 
import altair as alt
import numpy as np

# %%
# pulls data
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

# %%
# runs chart
chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)
chart

# %%
chart.save("intro_plot_code.png")

