import polars as pl
import matplotlib.pyplot as plt

CSV_URL = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"

def read_csv_and_count_rating():
    # Read the CSV data into a Polars DataFrame
    df = pl.read_csv(CSV_URL)
    df.drop_in_place('grape')
    print(df)
    rating_count = 0
    for _ in df['rating']:
        rating_count += 1
    rl = df['rating'].to_list()
    rating_sum = 0
    for n in rl:
        rating_sum += int(n)
    rating_avg = rating_sum/rating_count
    print(f"Count of rating is {rating_count}")
    print(f"Sum of rating is {rating_sum}")
    print(f"Average rating is {rating_avg}")
    return rating_count

def visualize_rating_histogram():
    # Read the CSV data into a Polars DataFrame
    df = pl.read_csv(CSV_URL)
    
    # Plot the histogram of the 'rating' column
    plt.hist(df['rating'].to_list(), bins=20, edgecolor='k')
    plt.xlabel('Wine Ratings')
    plt.ylabel('Frequency')
    plt.title('Distribution of Wine Ratings')
    plt.grid(True)
    plt.savefig("wine_rating.png", dpi=300)

visualize_rating_histogram()
read_csv_and_count_rating()
