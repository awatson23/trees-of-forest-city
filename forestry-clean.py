# %%
import pandas as pd

full = pd.read_csv('Forestry.csv')

full.head()

# %% remove anything after the comma in tree common name. ex: "Maple, Red" will now become "Maple"
full['CommonName'] = full['CommonName'].str.split(',').str[0]

print(full['CommonName'])

# %% count how many of each tree type and store into new dataset

fullCount = full['CommonName'].value_counts().reset_index()

# %% add columns for new data

fullCount.columns = ['tree_name', 'count']
print(fullCount)

# %% remove rows with vacant or unkown entry

fullCount = fullCount[fullCount.tree_name != 'Unknown']
fullCount = fullCount[fullCount.tree_name != 'Vacant']


# %% export tree type count without the index column
fullCount.to_csv('forest-city-tree-types.csv', index=False)

# %%
