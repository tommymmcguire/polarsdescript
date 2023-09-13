import polars as pl
import matplotlib.pyplot as plt

csv_url = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
df = pl.read_csv(csv_url, index_col=0)
df.drop(['grape'], axis=1, inplace=True)
print(df.describe())

def data_desc(csv_url):
    return df['rating'].count()


plt.hist(df['rating'], bins=20, edgecolor='k')
plt.xlabel('Wine Ratings')
plt.ylabel('Frequency')
plt.title('Distribution of Wine Ratings')
plt.grid(True)
plt.savefig("wine_rating.png", dpi=300)