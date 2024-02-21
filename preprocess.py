from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter
import pandas as pd
df=pd.read_csv("result.csv")
df = df[df['Rating'] != "Rating not found"]

df['Rating'] = df['Rating'].astype(float)
df['Price'] = df['Price'].str.replace('[^\d.]', '', regex=True)

df['Price'] = df['Price'].astype(float)
df['Ratio'] = df['Price'] / df['Rating']
import pandas as pd

df['Count'] = pd.to_numeric(df['Count'], errors='coerce')

first_quartile_count = df['Count'].quantile(0.25)

filtered_df = df[df['Count'] >= first_quartile_count]

filtered_df.reset_index(drop=True, inplace=True)

grouped_df = df.groupby('Ingredient')
max_counts = grouped_df['Count'].max() / 50
min_counts = grouped_df['Count'].min() / 50
scores = max_counts - min_counts
selected_ingredients = []
for ingredient, group in grouped_df:
    max_score_index = group['Count'].idxmax()
    selected_ingredients.append(df.loc[max_score_index])
selected_df = pd.DataFrame(selected_ingredients)
print(selected_df)
