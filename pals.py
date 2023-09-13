import polars as pl
import matplotlib.pyplot as plt

csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pl.read_csv(csv_url)

# Drop the 'grape' column
df = df.drop_in_place('grape')

# Get a description of the data
df.describe()

def data_desc(df):
    return df.select(pl.col('rating')).count().get(0)

# Plot the histogram
plt.hist(df['rating'].to_list(), bins=20, edgecolor='k')
plt.xlabel('Wine Ratings')
plt.ylabel('Frequency')
plt.title('Distribution of Wine Ratings')
plt.grid(True)
plt.savefig("wine_rating.png", dpi=300)




