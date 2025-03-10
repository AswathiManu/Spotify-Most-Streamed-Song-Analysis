#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


# importing CSV File
df = pd.read_csv("Spotify Most Streamed Songs.csv")


# ### Checking Data Types
# 

# In[6]:


data_types = df.dtypes
print(data_types)


# ### Checking Duplicates

# In[7]:


duplicates = df.duplicated().sum()
print(f'Total duplicates: {duplicates}')


# ###  Data Exploration

# In[8]:


# viewing the first few rows
df.head()


# In[9]:


df.info()


# In[10]:


# To view statisics
df.describe()


# In[11]:


# List all column names in the DataFrame
print(df.columns)


# In[13]:


# Get the shape of the DataFrame (rows, columns)
df.shape


# In[14]:


# Identify missing values in the DataFrame
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])  # Show only columns with missing values


# In[15]:


# Drop rows with any missing values
df_cleaned = df.dropna()

# Drop columns with any missing values
df_cleaned = df.dropna(axis=1)


# ### Data Cleaning

# In[16]:


from scipy import stats

# Calculate Z-scores of each value in the DataFrame
z_scores = stats.zscore(df.select_dtypes(include=['float64', 'int64']))

# Identify outliers (Z-score > 3 or < -3)
df_outliers = df[(z_scores > 3).any(axis=1) | (z_scores < -3).any(axis=1)]
print(f'Number of outliers detected: {df_outliers.shape[0]}')


# In[17]:


# Remove rows with outliers based on Z-score
df_no_outliers = df[(z_scores < 3).all(axis=1) & (z_scores > -3).all(axis=1)]


# ## Analysing the Dataframe
# ### How does danceability correlate with streams for the songs?

# In[18]:


import plotly.express as px

# Scatter plot for danceability vs streams
fig2 = px.scatter(df_no_outliers, 
                  x='danceability_%', 
                  y='streams', 
                  color='artist_count',
                  hover_data=['track_name', 'artist(s)_name'],
                  title='Danceability vs Streams',
                  color_continuous_scale='Bluered')
fig2.show()


# ### What is the distribution of BPM (Beats Per Minute) in the dataset?

# In[19]:


# Histogram for BPM distribution
fig3 = px.histogram(df_no_outliers, 
                    x='bpm', 
                    title='Distribution of BPM',
                    color='released_year',
                    color_discrete_sequence=px.colors.qualitative.Prism)
fig3.show()


# ### What does the correlation heatmap reveal about the features in the dataset?

# In[22]:


import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlation matrix
correlation_matrix = df_no_outliers.select_dtypes(include=['float64', 'int64']).corr()

# Create heatmap for correlation
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='magma')
plt.title('Correlation Heatmap - magma')
plt.show()


# ### How do energy levels vary with danceability percentages?

# In[25]:


# Scatter plot for energy vs danceability
fig = px.scatter(df_no_outliers, 
                  x='danceability_%', 
                  y='energy_%', 
                  color='released_year', 
                  hover_data=['track_name', 'artist(s)_name'],
                  title='Energy Levels vs Danceability',
                  color_continuous_scale='Turbo')
fig.show()


# ### How do different song attributes correlate with each other?

# In[31]:


# Pair plot for selected numerical features
import plotly.express as px

fig = px.scatter_matrix(df_no_outliers,
                          dimensions=['danceability_%', 'energy_%', 'valence_%', 'acousticness_%', 'bpm'],
                          title='Pair Plot of Selected Features',
                          color='released_year',
                          color_continuous_scale='Turbo')
fig.show()


# ### What are the trends in song releases over the years?

# In[38]:


# Line chart showing the trend of song releases by year
release_trends = df_no_outliers['released_year'].value_counts().sort_index().reset_index()
release_trends.columns = ['released_year', 'song_count']

fig = px.line(release_trends, 
                x='released_year', 
                y='song_count', 
                title='Trends in Song Releases Over the Years',
                markers=True,
                #color='song_count',
                line_shape='linear')

# Customize the line color
fig.update_traces(line_color='purple')

fig.show()


# ### What is the relationship between liveness and streams for the songs?

# In[43]:


# Scatter plot for liveness vs streams
fig = px.scatter(df_no_outliers, 
                  x='liveness_%', 
                  y='streams', 
                  color='released_year',
                  hover_data=['track_name', 'artist(s)_name'],
                  title='Liveness vs Streams',
                  color_continuous_scale='Cividis')
fig.show()


# In[45]:


print(df.dtypes)
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
print(df['streams'].isnull().sum())


# In[53]:


df = df.dropna(subset=['streams'])
top_artists = df.groupby('artist(s)_name')['streams'].sum().reset_index().sort_values(by='streams', ascending=False)
plt.figure(figsize=(12,8))
sns.barplot(x='streams', y='artist(s)_name', data=top_artists.head(10), palette='plasma')
plt.title('Top 10 Most Streamed Artists')
plt.xlabel('Total Streams')
plt.ylabel('Artist')
plt.show()


# In[52]:


print(top_artists.head(10)) 


# In[ ]:




