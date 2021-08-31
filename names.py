# %%
#Imports data and libraries
import pandas as pd 
import numpy as np 
import altair as alt 
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
dat = pd.read_csv(url)

# %%
# How many unique names do we have?
pd.unique(dat.name).size
len(pd.unique(dat.name))

# %%
# How many times does my name show up?
dat.query('name == "Austin"').year.size

# %%
# Which names have been 
# given the most and the least?
# https://byuidatascience.github.io/python4ds/transform.html#grouped-summaries-or-aggregations-with-.agg
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
dat_name = (dat.groupby(['name'])
    .agg(Total_all = ('Total', np.sum),
        Average_all = ("Total", np.mean))
    .reset_index())
dat_name.sort_values('Total_all').head(1).name
dat_name.sort_values('Total_all').tail(1).name

# %%
# Shows the most popular and least popular names in Utah
dat_name_state = (dat.groupby(['name'])
    .agg(Total_all = ('UT', np.sum),
        Average_all = ("UT", np.mean))
    .reset_index()
    .query("Total_all > 0")
    .sort_values("Total_all"))
print(dat_name_state.head(1).name)
dat_name_state.tail(1).name

# %%
# Graphs most popular names in utah
(alt.Chart(dat_name_state.tail(25))
    .encode(
        x = alt.X('name', sort='-y'), 
        y = "Total_all")
    .mark_bar())

# %%
# Creates graph of the occurance of my name
chart = (alt.Chart(dat.query("name ==  'Austin'"),
 title = "The occurances of 'Austin")
    .encode(
        alt.X("year", axis=alt.Axis(format='.0f'), title = "Year of Birth"),
        alt.Y("Total", title="Number of Austin Births"),
        alt.Color("name")
    )
    .mark_line())
chart

# %%
# Creates data frame that shows my name historicialy over the years
dat_line = pd.DataFrame({
    "year":[1998],
    "name": ["Austin"],
    "label": ["Birth Year"],
    "y": [1000]
})
line_chart = alt.Chart(dat_line).encode(x = "year", color="name").mark_rule()
label_chart = alt.Chart(dat_line).encode(
    x = "year", 
    y = "y", 
    text = "label",
    color = "name").mark_text(dx=35)
chart_name = chart + label_chart + line_chart
chart_name.save("my_name_chart.png")

# %%
# Creates dataframe that shows the use of Brittany over the years
# Shows average birth year for brittany
dat_name_brittany = (dat
  .groupby(['name', 'year'])
  .sum()
  .query('name == "Brittany"')
  .reset_index()
  .filter(['name', 'year', 'Total'])
  .sort_values('Total'))

df = pd.DataFrame(dat_name_brittany)

# brittany_chart = df.plot.bar(x='year',
# title = "Instances of Brittany")
brittany_chart_graph = (alt.Chart(dat.query("name ==  'Brittany'"),
 title = "The occurances of 'Brittany")
    .encode(
        alt.X("year", axis=alt.Axis(format='.0f'), title = "Year of Birth"),
        alt.Y("Total", title="Number of brittany Births"),
        color=alt.value("#FFAA00")
    )
    .mark_line())

dat_line_brittany = pd.DataFrame({
    "year":[1996, 1986],
    "name": ["Guess", "Guess"],
    "label": ["Guess", "Guess"],
    "y": [1000, 1000]
})

line_brittany = alt.Chart(dat_line_brittany).encode(x = "year", color="name").mark_rule()
brittany_chart = brittany_chart_graph + line_brittany

# %%
# Saves chart for brittany
brittany_chart.save("brittany_chart.png")

# %% 
# creates data frame for christian names
chart_cr = dat.query("name in ['Mary', 'Martha', 'Peter', 'Paul'] & (year >= 1920 & year <= 2000)")

# %%
# creates and saves christian chart
(alt.Chart(chart_cr,
 title = "The occurances of Christian names")
    .encode(
        alt.X('year:Q', axis=alt.Axis(format='.0f'), title = "Year"),
        alt.Y("Total", title="Number of new babies with christian names"),
        alt.Color("name"),
    )
    .mark_line().save("christian_chart.png"))

# %%
# creates chart for luke
arnold_chart = (alt.Chart(dat.query("name ==  'Luke' & (year >= 1970 & year <= 2000)"),
 title = "Popularity of the name luke from Star Wars between 1970 and 2000")
    .encode(
        alt.X("year", axis=alt.Axis(format='.0f'), title = "Year"),
        alt.Y("Total", title="Number of new babies named Luke"),
        alt.Color("name")
    )
    .mark_line())

# %% 
# creates dataframe and combines chart data
dat_line_arnold = pd.DataFrame({
    "year":[1977],
    "name": ["Luke"],
    "label": ["First Star Wars Movie Release"],
    "y": [1000]
})
line_chart_arnold = alt.Chart(dat_line_arnold).encode(x = "year", color="name").mark_rule()
label_chart_arnold = alt.Chart(dat_line_arnold).encode(
    x = "year", 
    y = "y", 
    text = "label",
    color = "name").mark_text(dx=35)
chart_arnold = arnold_chart + label_chart_arnold + line_chart_arnold

# %%
# Saves chart for arnold
chart_arnold.save("arnold_chart.png")

# %%

