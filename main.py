
import polars as pl
import matplotlib.pyplot as plt

CSV_URL = "https://raw.githubusercontent.com/paiml/wine-ratings/main/wine-ratings.csv"
OUTPUT_FILE = "output.md"  # Specify the Markdown file name
HISTOGRAM_IMAGE_FILE = "wine_rating.png"  # Specify the histogram image file name

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

    median_rating = df['rating'].median()
    stddev_rating = df['rating'].std()
    # Print the results
    print(f"Median rating is {median_rating}")
    print(f"Standard deviation of ratings is {stddev_rating}")

    # Open the Markdown file for writing
    with open(OUTPUT_FILE, 'w') as markdown_file:
        markdown_file.write(f"Count of rating is: {rating_count}\n\n")
        markdown_file.write(f"Sum of rating is: {rating_sum}\n\n")
        markdown_file.write(f"Average rating is: {rating_avg}\n\n")
        markdown_file.write(f"Median of rating is: {median_rating}\n\n")
        markdown_file.write(f"Standard deviation of rating is: {stddev_rating}\n\n")

    return rating_count, rating_avg, median_rating, stddev_rating


def visualize_rating_histogram():
    # Read the CSV data into a Polars DataFrame
    df = pl.read_csv(CSV_URL)
    
    # Plot the histogram of the 'rating' column
    plt.hist(df['rating'].to_list(), bins=20, edgecolor='k')
    plt.xlabel('Wine Ratings')
    plt.ylabel('Frequency')
    plt.title('Distribution of Wine Ratings')
    plt.grid(True)
    plt.savefig(HISTOGRAM_IMAGE_FILE, dpi=300)
    
    # Append the histogram image to the Markdown file using 'a' mode
    with open(OUTPUT_FILE, 'a') as markdown_file:
        markdown_file.write("\n![Histogram](wine_rating.png)\n")

visualize_rating_histogram()
read_csv_and_count_rating()
