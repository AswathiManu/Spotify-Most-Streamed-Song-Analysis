# Spotify Most Streamed Songs Analysis

## Project Overview
This project analyzes the most streamed songs on Spotify to uncover trends and relationships between various musical attributes. It includes data exploration, cleaning, visualization, and statistical insights into the dataset.

## Dataset
The dataset used for this analysis is **Spotify Most Streamed Songs.csv**, containing information on various attributes such as:
- Track Name
- Artist(s) Name
- Streams
- Danceability
- Energy
- BPM (Beats Per Minute)
- Valence
- Acousticness
- Released Year

## Objectives
- Explore and clean the dataset.
- Identify trends and patterns in streaming data.
- Perform statistical and visual analysis of song attributes.
- Understand correlations between features like danceability, energy, and streams.
- Identify top artists based on total streams.

## Data Preprocessing & Cleaning
1. **Checking Data Types**: Ensured appropriate data types for each column.
2. **Checking for Duplicates**: Identified and removed duplicate entries.
3. **Handling Missing Values**:
   - Identified columns with missing values.
   - Dropped rows/columns where necessary.
4. **Outlier Detection & Removal**:
   - Used Z-score to detect and remove extreme values.

## Exploratory Data Analysis (EDA)
### Key Visualizations & Insights
1. **Danceability vs Streams**:
   - Scatter plot to analyze how danceability affects streaming numbers.
2. **BPM Distribution**:
   - Histogram to observe the distribution of beats per minute across songs.
3. **Correlation Heatmap**:
   - Visualizing feature correlations to identify strong relationships.
4. **Energy vs Danceability**:
   - Scatter plot to see how energetic a song is in relation to its danceability.
5. **Pair Plot of Selected Features**:
   - Understanding how different song attributes interact.
6. **Trends in Song Releases Over the Years**:
   - Line chart displaying trends in song releases over time.
7. **Liveness vs Streams**:
   - Scatter plot to explore how live performances affect streaming numbers.
8. **Top 10 Most Streamed Artists**:
   - Bar chart showing the artists with the highest total streams.

## Technologies & Libraries Used
- **Python** (Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly)
- **Jupyter Notebook**

## Results & Key Takeaways
- Danceability and energy have a strong impact on the popularity of songs.
- Songs released in recent years tend to have higher streaming numbers.
- BPM follows a specific distribution, influencing song preferences.
- Correlations between attributes like danceability, valence, and acousticness provide insights into music composition trends.
- Some artists consistently dominate the top-streamed charts.

## Future Enhancements
- Expanding analysis to include more datasets.
- Applying machine learning techniques for predictive analytics.
- Building an interactive dashboard for real-time data exploration.

## Author
This project was conducted as part of an in-depth exploratory data analysis to uncover meaningful insights from Spotify streaming data.

---
### References
- Spotify API (For possible future extensions)
- Official Spotify Charts

Thank you for exploring this project! 🚀
